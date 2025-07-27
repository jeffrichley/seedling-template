# TimelineBuilder Specification

> **Project:** Vine Media Framework
> **Component:** TimelineBuilder
> **Status:** Ready for Implementation
> **Priority:** High
> **Timeline:** Week 1-2

## Overview

The TimelineBuilder provides a fluent, chainable API for constructing video timelines in Project Vine. It supports both scene-based and beat-driven editing modes, with seamless voice-image pair synchronization and comprehensive validation.

## Core Architecture

### TimelineBuilder (Main Class)

**Purpose:** Primary interface for timeline construction

```python
from typing import List, Dict, Any, Optional, Union
from pathlib import Path
from moviepy.editor import VideoClip, AudioFileClip, ImageClip
from .models import TimelineSpec, SceneSpec, AudioSpec, VideoSpec

class TimelineBuilder:
    """Fluent API for video timeline construction."""

    def __init__(self):
        self._timeline = TimelineSpec()
        self._scenes: Dict[str, SceneSpec] = {}
        self._current_scene: Optional[str] = None
        self._registry_manager = RegistryManager()
        self._validation_enabled = True

    def set_mode(self, mode: Literal["scene", "beat", "hybrid"]) -> "TimelineBuilder":
        """Set the timeline editing mode."""
        self._timeline.mode = mode
        return self

    def set_duration(self, duration: float) -> "TimelineBuilder":
        """Set the total timeline duration."""
        if duration <= 0:
            raise ValueError("Duration must be positive")
        self._timeline.duration = duration
        return self

    def set_fps(self, fps: float) -> "TimelineBuilder":
        """Set the timeline frame rate."""
        if fps <= 0 or fps > 120:
            raise ValueError("FPS must be between 0 and 120")
        self._timeline.fps = fps
        return self

    def add_scene(self, scene_id: str, duration: float,
                  name: Optional[str] = None) -> "TimelineBuilder":
        """Add a new scene to the timeline."""
        if scene_id in self._scenes:
            raise ValueError(f"Scene '{scene_id}' already exists")

        scene = SceneSpec(
            id=scene_id,
            name=name or scene_id,
            duration=duration,
            start_time=self._calculate_scene_start_time()
        )

        self._scenes[scene_id] = scene
        self._timeline.scenes.append(scene)
        self._current_scene = scene_id
        return self

    def add_voice_image_pair(self, scene_id: str, voice_file: Union[str, Path],
                            image_file: Union[str, Path],
                            sync_offset: float = 0.0) -> "TimelineBuilder":
        """Add a voice-image pair to a scene."""
        if scene_id not in self._scenes:
            raise ValueError(f"Scene '{scene_id}' not found")

        scene = self._scenes[scene_id]

        # Create voice-image pair
        pair = VoiceImagePairSpec(
            id=f"{scene_id}_pair",
            voice_file=Path(voice_file),
            image_file=Path(image_file),
            start_time=scene.start_time,
            voice_duration=scene.duration,
            image_duration=scene.duration,
            sync_offset=sync_offset
        )

        # Add to scene
        scene.audio = AudioClipSpec(
            file_path=pair.voice_file,
            start_time=scene.start_time,
            duration=scene.duration,
            volume=1.0
        )

        scene.images.append(ImageClipSpec(
            file_path=pair.image_file,
            start_time=scene.start_time,
            duration=scene.duration
        ))

        return self

    def add_effect(self, target: str, effect_type: str,
                   parameters: Dict[str, Any]) -> "TimelineBuilder":
        """Add an effect to a scene or element."""
        if target not in self._scenes:
            raise ValueError(f"Target '{target}' not found")

        # Validate effect type
        if not self._registry_manager.get_registry("effects").list():
            raise ValueError(f"Effect type '{effect_type}' not available")

        effect = EffectSpec(
            type=effect_type,
            target=target,
            start_time=self._scenes[target].start_time,
            duration=self._scenes[target].duration,
            parameters=parameters
        )

        self._scenes[target].effects.append(effect)
        return self

    def add_transition(self, from_scene: str, to_scene: str,
                       transition_type: str,
                       parameters: Dict[str, Any]) -> "TimelineBuilder":
        """Add a transition between scenes."""
        if from_scene not in self._scenes or to_scene not in self._scenes:
            raise ValueError("Both scenes must exist")

        # Validate transition type
        if not self._registry_manager.get_registry("transitions").list():
            raise ValueError(f"Transition type '{transition_type}' not available")

        transition = TransitionSpec(
            type=transition_type,
            from_scene=from_scene,
            to_scene=to_scene,
            parameters=parameters
        )

        self._timeline.transitions.append(transition)
        return self

    def add_beat_section(self, section_id: str, beats: List[int],
                         audio_file: Union[str, Path],
                         image_files: List[Union[str, Path]]) -> "TimelineBuilder":
        """Add a beat-driven section to the timeline."""
        if self._timeline.mode not in ["beat", "hybrid"]:
            raise ValueError("Beat sections require beat or hybrid mode")

        # Calculate timing based on beats
        beat_timing = self._calculate_beat_timing(beats)

        # Create beat specifications
        beat_specs = []
        for i, beat in enumerate(beats):
            beat_spec = BeatSpec(
                beat_number=beat,
                start_time=beat_timing[i],
                duration=beat_timing[i+1] - beat_timing[i] if i < len(beat_timing)-1 else 1.0
            )
            beat_specs.append(beat_spec)

        self._timeline.beats.extend(beat_specs)
        return self

    def set_audio(self, voice_track: Optional[Union[str, Path]] = None,
                  background_music: Optional[Union[str, Path]] = None,
                  volume: float = 1.0) -> "TimelineBuilder":
        """Set audio configuration for the timeline."""
        audio_spec = AudioSpec(volume=volume)

        if voice_track:
            audio_spec.voice_track = AudioClipSpec(
                file_path=Path(voice_track),
                start_time=0.0,
                duration=self._timeline.total_duration,
                volume=volume
            )

        if background_music:
            audio_spec.background_music = AudioClipSpec(
                file_path=Path(background_music),
                start_time=0.0,
                duration=self._timeline.total_duration,
                volume=volume * 0.3  # Background music at 30% volume
            )

        self._timeline.audio = audio_spec
        return self

    def disable_validation(self) -> "TimelineBuilder":
        """Disable validation for performance."""
        self._validation_enabled = False
        return self

    def enable_validation(self) -> "TimelineBuilder":
        """Enable validation."""
        self._validation_enabled = True
        return self

    def build(self) -> VideoSpec:
        """Build the final video specification."""
        if self._validation_enabled:
            self._validate_timeline()

        return VideoSpec(
            timeline=self._timeline,
            audio=self._timeline.audio or AudioSpec(),
            export=self._create_default_export()
        )

    def _calculate_scene_start_time(self) -> float:
        """Calculate start time for the next scene."""
        if not self._timeline.scenes:
            return 0.0
        return max(scene.end_time for scene in self._timeline.scenes)

    def _calculate_beat_timing(self, beats: List[int]) -> List[float]:
        """Calculate timing for beat sequence."""
        # Simplified beat timing calculation
        # In practice, this would use actual beat detection
        total_beats = max(beats)
        duration_per_beat = self._timeline.duration / total_beats if self._timeline.duration else 1.0
        return [beat * duration_per_beat for beat in beats]

    def _validate_timeline(self):
        """Validate the timeline configuration."""
        # Validate scene sequence
        if len(self._timeline.scenes) > 1:
            for i, scene in enumerate(self._timeline.scenes[1:], 1):
                if scene.start_time <= self._timeline.scenes[i-1].end_time:
                    raise ValueError(f"Scene {i} starts before previous scene ends")

        # Validate transitions
        for transition in self._timeline.transitions:
            if transition.from_scene not in self._scenes:
                raise ValueError(f"Transition references non-existent scene: {transition.from_scene}")
            if transition.to_scene not in self._scenes:
                raise ValueError(f"Transition references non-existent scene: {transition.to_scene}")

        # Validate effects
        for scene in self._timeline.scenes:
            for effect in scene.effects:
                if effect.target not in self._scenes:
                    raise ValueError(f"Effect targets non-existent scene: {effect.target}")

    def _create_default_export(self) -> ExportSpec:
        """Create default export configuration."""
        return ExportSpec(
            output_path=Path("output.mp4"),
            format="mp4",
            resolution=(1920, 1080),
            fps=self._timeline.fps,
            quality="high"
        )
```

### SceneBuilder (Scene-Specific Operations)

**Purpose:** Specialized builder for scene-level operations

```python
class SceneBuilder:
    """Specialized builder for scene-level operations."""

    def __init__(self, timeline_builder: TimelineBuilder, scene_id: str):
        self._timeline_builder = timeline_builder
        self._scene_id = scene_id

    def add_image(self, image_file: Union[str, Path],
                  start_time: float = 0.0, duration: float = None) -> "SceneBuilder":
        """Add an image to the current scene."""
        if self._scene_id not in self._timeline_builder._scenes:
            raise ValueError(f"Scene '{self._scene_id}' not found")

        scene = self._timeline_builder._scenes[self._scene_id]
        if duration is None:
            duration = scene.duration - start_time

        image_clip = ImageClipSpec(
            file_path=Path(image_file),
            start_time=scene.start_time + start_time,
            duration=duration
        )

        scene.images.append(image_clip)
        return self

    def add_audio(self, audio_file: Union[str, Path],
                  start_time: float = 0.0, duration: float = None,
                  volume: float = 1.0) -> "SceneBuilder":
        """Add audio to the current scene."""
        if self._scene_id not in self._timeline_builder._scenes:
            raise ValueError(f"Scene '{self._scene_id}' not found")

        scene = self._timeline_builder._scenes[self._scene_id]
        if duration is None:
            duration = scene.duration - start_time

        audio_clip = AudioClipSpec(
            file_path=Path(audio_file),
            start_time=scene.start_time + start_time,
            duration=duration,
            volume=volume
        )

        scene.audio = audio_clip
        return self

    def add_effect(self, effect_type: str,
                   parameters: Dict[str, Any]) -> "SceneBuilder":
        """Add an effect to the current scene."""
        return self._timeline_builder.add_effect(self._scene_id, effect_type, parameters)

    def set_transition_in(self, transition_type: str,
                          parameters: Dict[str, Any]) -> "SceneBuilder":
        """Set the transition into this scene."""
        scene = self._timeline_builder._scenes[self._scene_id]
        scene.transition_in = TransitionSpec(
            type=transition_type,
            from_scene="",  # Will be set by timeline builder
            to_scene=self._scene_id,
            parameters=parameters
        )
        return self

    def set_transition_out(self, transition_type: str,
                           parameters: Dict[str, Any]) -> "SceneBuilder":
        """Set the transition out of this scene."""
        scene = self._timeline_builder._scenes[self._scene_id]
        scene.transition_out = TransitionSpec(
            type=transition_type,
            from_scene=self._scene_id,
            to_scene="",  # Will be set by timeline builder
            parameters=parameters
        )
        return self

    def end_scene(self) -> TimelineBuilder:
        """End scene editing and return to timeline builder."""
        return self._timeline_builder
```

### BeatBuilder (Beat-Driven Operations)

**Purpose:** Specialized builder for beat-driven editing

```python
class BeatBuilder:
    """Specialized builder for beat-driven editing."""

    def __init__(self, timeline_builder: TimelineBuilder):
        self._timeline_builder = timeline_builder
        self._current_beat = 0

    def set_beat_mode(self, enabled: bool = True) -> "BeatBuilder":
        """Enable or disable beat mode."""
        if enabled:
            self._timeline_builder.set_mode("beat")
        return self

    def add_beat_section(self, section_id: str, beats: List[int],
                         audio_file: Union[str, Path],
                         image_files: List[Union[str, Path]]) -> "BeatBuilder":
        """Add a beat section with synchronized audio and images."""
        return self._timeline_builder.add_beat_section(
            section_id, beats, audio_file, image_files
        )

    def add_beat_effect(self, beat_number: int, effect_type: str,
                        parameters: Dict[str, Any]) -> "BeatBuilder":
        """Add an effect to a specific beat."""
        # Find the beat specification
        beat_spec = None
        for beat in self._timeline_builder._timeline.beats:
            if beat.beat_number == beat_number:
                beat_spec = beat
                break

        if not beat_spec:
            raise ValueError(f"Beat {beat_number} not found")

        # Add effect to the beat
        effect = EffectSpec(
            type=effect_type,
            target=f"beat_{beat_number}",
            start_time=beat_spec.start_time,
            duration=beat_spec.duration,
            parameters=parameters
        )

        # Store effect for later application
        if not hasattr(self._timeline_builder, '_beat_effects'):
            self._timeline_builder._beat_effects = {}

        if beat_number not in self._timeline_builder._beat_effects:
            self._timeline_builder._beat_effects[beat_number] = []

        self._timeline_builder._beat_effects[beat_number].append(effect)
        return self

    def set_beat_timing(self, bpm: float) -> "BeatBuilder":
        """Set the beats per minute for timing calculations."""
        self._timeline_builder._bpm = bpm
        return self

    def end_beat_mode(self) -> TimelineBuilder:
        """End beat mode and return to timeline builder."""
        return self._timeline_builder
```

## API Usage Examples

### Basic Scene-Based Editing

```python
# Create a simple video with voice-image pairs
video_spec = (
    TimelineBuilder()
    .set_mode("scene")
    .set_duration(10.0)
    .add_scene("intro", 3.0, "Introduction")
    .add_voice_image_pair("intro", "intro_audio.mp3", "intro_image.jpg")
    .add_effect("intro", "ken_burns", {"zoom": 1.2})
    .add_scene("main", 5.0, "Main Content")
    .add_voice_image_pair("main", "main_audio.mp3", "main_image.jpg")
    .add_effect("main", "slide", {"direction": "left"})
    .add_transition("intro", "main", "fade", {"duration": 0.5})
    .add_scene("outro", 2.0, "Conclusion")
    .add_voice_image_pair("outro", "outro_audio.mp3", "outro_image.jpg")
    .add_transition("main", "outro", "crossfade", {"duration": 0.3})
    .build()
)
```

### Beat-Driven Editing

```python
# Create a beat-synchronized video
video_spec = (
    TimelineBuilder()
    .set_mode("beat")
    .set_duration(8.0)
    .set_beat_timing(120.0)  # 120 BPM
    .add_beat_section("verse", [1, 2, 3, 4], "verse_audio.mp3",
                      ["verse_1.jpg", "verse_2.jpg", "verse_3.jpg", "verse_4.jpg"])
    .add_beat_effect(2, "zoom", {"scale": 1.1})
    .add_beat_effect(4, "slide", {"direction": "right"})
    .build()
)
```

### Hybrid Mode

```python
# Create a hybrid scene/beat video
video_spec = (
    TimelineBuilder()
    .set_mode("hybrid")
    .set_duration(15.0)
    .add_scene("intro", 3.0)
    .add_voice_image_pair("intro", "intro_audio.mp3", "intro_image.jpg")
    .add_beat_section("chorus", [1, 2, 3, 4], "chorus_audio.mp3",
                      ["chorus_1.jpg", "chorus_2.jpg", "chorus_3.jpg", "chorus_4.jpg"])
    .add_scene("outro", 2.0)
    .add_voice_image_pair("outro", "outro_audio.mp3", "outro_image.jpg")
    .build()
)
```

### Advanced Scene Building

```python
# Use scene builder for complex scenes
video_spec = (
    TimelineBuilder()
    .set_mode("scene")
    .add_scene("complex_scene", 5.0)
    .scene("complex_scene")
        .add_image("background.jpg", 0.0, 5.0)
        .add_image("overlay.png", 1.0, 3.0)
        .add_audio("voice.mp3", 0.0, 5.0, 1.0)
        .add_audio("music.mp3", 0.0, 5.0, 0.3)
        .add_effect("ken_burns", {"zoom": 1.1, "pan_x": 0.1})
        .set_transition_in("fade", {"duration": 0.5})
        .set_transition_out("slide", {"direction": "left"})
        .end_scene()
    .build()
)
```

## Validation and Error Handling

### Timeline Validation

```python
def validate_timeline(timeline: TimelineSpec) -> List[str]:
    """Validate timeline and return list of errors."""
    errors = []

    # Check scene sequence
    for i, scene in enumerate(timeline.scenes[1:], 1):
        if scene.start_time <= timeline.scenes[i-1].end_time:
            errors.append(f"Scene {i} overlaps with previous scene")

    # Check effect timing
    for scene in timeline.scenes:
        for effect in scene.effects:
            if effect.start_time < scene.start_time:
                errors.append(f"Effect starts before scene: {effect.type}")
            if effect.end_time > scene.end_time:
                errors.append(f"Effect extends beyond scene: {effect.type}")

    # Check transition references
    scene_ids = {scene.id for scene in timeline.scenes}
    for transition in timeline.transitions:
        if transition.from_scene not in scene_ids:
            errors.append(f"Transition references non-existent scene: {transition.from_scene}")
        if transition.to_scene not in scene_ids:
            errors.append(f"Transition references non-existent scene: {transition.to_scene}")

    return errors
```

### Error Recovery

```python
class TimelineBuilderError(Exception):
    """Base exception for timeline builder errors."""
    pass

class ValidationError(TimelineBuilderError):
    """Raised when timeline validation fails."""
    pass

class ConfigurationError(TimelineBuilderError):
    """Raised when configuration is invalid."""
    pass

def safe_build(builder: TimelineBuilder) -> VideoSpec:
    """Safely build timeline with error recovery."""
    try:
        return builder.build()
    except ValidationError as e:
        # Attempt to fix common issues
        builder = _attempt_fix(builder, e)
        return builder.build()
    except Exception as e:
        raise TimelineBuilderError(f"Failed to build timeline: {e}")

def _attempt_fix(builder: TimelineBuilder, error: ValidationError) -> TimelineBuilder:
    """Attempt to fix common timeline issues."""
    # Implementation of common fixes
    return builder
```

## Performance Optimization

### Lazy Evaluation

```python
class LazyTimelineBuilder(TimelineBuilder):
    """Timeline builder with lazy evaluation."""

    def __init__(self):
        super().__init__()
        self._operations = []
        self._built = False

    def add_scene(self, scene_id: str, duration: float,
                  name: Optional[str] = None) -> "LazyTimelineBuilder":
        """Add scene operation to queue."""
        self._operations.append(("add_scene", scene_id, duration, name))
        return self

    def build(self) -> VideoSpec:
        """Execute all operations and build timeline."""
        if self._built:
            return self._video_spec

        # Execute operations
        for op, *args in self._operations:
            getattr(super(), op)(*args)

        self._video_spec = super().build()
        self._built = True
        return self._video_spec
```

### Caching

```python
class CachedTimelineBuilder(TimelineBuilder):
    """Timeline builder with caching."""

    def __init__(self):
        super().__init__()
        self._cache = {}

    def _get_cache_key(self, operation: str, *args) -> str:
        """Generate cache key for operation."""
        return f"{operation}:{hash(str(args))}"

    def add_scene(self, scene_id: str, duration: float,
                  name: Optional[str] = None) -> "CachedTimelineBuilder":
        """Add scene with caching."""
        cache_key = self._get_cache_key("add_scene", scene_id, duration, name)

        if cache_key in self._cache:
            # Return cached result
            return self._cache[cache_key]

        # Execute operation
        result = super().add_scene(scene_id, duration, name)
        self._cache[cache_key] = result
        return result
```

## Testing Strategy

### Unit Tests

1. **Basic Operations**: Test all builder methods
2. **Method Chaining**: Test fluent API chaining
3. **Validation**: Test timeline validation
4. **Error Handling**: Test error scenarios
5. **Mode Switching**: Test scene/beat/hybrid modes

### Integration Tests

1. **End-to-End**: Test complete timeline building
2. **Registry Integration**: Test effect/transition integration
3. **Model Integration**: Test Pydantic model integration
4. **Performance**: Test builder performance

### Performance Tests

1. **Large Timelines**: Test with many scenes/effects
2. **Memory Usage**: Test memory consumption
3. **Build Time**: Test timeline build performance
4. **Cache Effectiveness**: Test caching performance

## Documentation Requirements

1. **API Reference**: Complete method documentation
2. **Usage Examples**: Comprehensive examples
3. **Best Practices**: Recommended usage patterns
4. **Performance Guide**: Optimization tips
5. **Migration Guide**: Version migration notes
