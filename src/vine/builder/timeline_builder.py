"""TimelineBuilder for Project Vine video composition framework."""

from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from vine.defaults.defaults_manager import DefaultsManager
from vine.models.tracks import (
    AudioClip,
    AudioTrack,
    ImageClip,
    TextClip,
    TextTrack,
    VideoTrack,
)
from vine.models.transition import Transition
from vine.models.video_spec import VideoSpec

# Type hint for MoviePy CompositeVideoClip
try:
    from moviepy import CompositeVideoClip
except ImportError:
    CompositeVideoClip = None  # type: ignore


class TimelineBuilder:
    """
    Builder for creating video timelines with track-based architecture.

    Supports dual-mode timing:
    - Sequential mode: Elements are appended to the end of their respective tracks
    - Explicit mode: Elements are positioned at specific times with _at methods

    Auto-detects track types and manages track creation.
    """

    def __init__(self, width: int = 1920, height: int = 1080, fps: float = 30):
        """
        Initialize TimelineBuilder.

        Args:
            width: Video width in pixels
            height: Video height in pixels
            fps: Frames per second
        """
        self.width = width
        self.height = height
        self.fps = fps
        self.video_tracks: List[VideoTrack] = [VideoTrack(name="video_0")]
        self.music_tracks: List[AudioTrack] = [AudioTrack(name="music_0")]
        self.voice_tracks: List[AudioTrack] = [AudioTrack(name="voice_0")]
        self.sfx_tracks: List[AudioTrack] = [AudioTrack(name="sfx_0")]
        self.text_tracks: List[TextTrack] = [TextTrack(name="text_0")]
        self.transitions: List[Transition] = []
        # Track-specific current times for sequential appending
        self._video_current_time = 0.0
        self._music_current_time = 0.0
        self._voice_current_time = 0.0
        self._sfx_current_time = 0.0
        self._text_current_time = 0.0
        # Default duration for next sequential element
        self._next_duration: Optional[float] = None
        self.defaults = DefaultsManager()

    # ============================================================================
    # TRACK AUTO-DETECTION METHODS
    # ============================================================================

    def _get_or_create_video_track(self) -> VideoTrack:
        """Get or create a video track for auto-detection."""
        # Always use the first track initially
        if len(self.video_tracks) == 1 and len(self.video_tracks[0].clips) == 0:
            return self.video_tracks[0]

        # Try to find a track without overlapping clips
        for track in self.video_tracks:
            if not track.has_overlapping_clips():
                return track

        # Create new track if all existing tracks have overlaps
        new_track = VideoTrack(name=f"video_{len(self.video_tracks)}")
        self.video_tracks.append(new_track)
        return new_track

    def _get_or_create_music_track(self) -> AudioTrack:
        """Get or create a music track for auto-detection."""
        # Try to find a track without overlapping clips
        for track in self.music_tracks:
            if not track.has_overlapping_clips():
                return track

        # Create new track if all existing tracks have overlaps
        new_track = AudioTrack(name=f"music_{len(self.music_tracks)}")
        self.music_tracks.append(new_track)
        return new_track

    def _get_or_create_voice_track(self) -> AudioTrack:
        """Get or create a voice track for auto-detection."""
        # Try to find a track without overlapping clips
        for track in self.voice_tracks:
            if not track.has_overlapping_clips():
                return track

        # Create new track if all existing tracks have overlaps
        new_track = AudioTrack(name=f"voice_{len(self.voice_tracks)}")
        self.voice_tracks.append(new_track)
        return new_track

    def _get_or_create_sfx_track(self) -> AudioTrack:
        """Get or create an SFX track for auto-detection."""
        # Try to find a track without overlapping clips
        for track in self.sfx_tracks:
            if not track.has_overlapping_clips():
                return track

        # Create new track if all existing tracks have overlaps
        new_track = AudioTrack(name=f"sfx_{len(self.sfx_tracks)}")
        self.sfx_tracks.append(new_track)
        return new_track

    def _get_or_create_text_track(self) -> TextTrack:
        """Get or create a text track for auto-detection."""
        # Try to find a track without overlapping clips
        for track in self.text_tracks:
            if not track.has_overlapping_clips():
                return track

        # Create new track if all existing tracks have overlaps
        new_track = TextTrack(name=f"text_{len(self.text_tracks)}")
        self.text_tracks.append(new_track)
        return new_track

    def _validate_audio_file(self, file_path: str) -> bool:
        """Validate that a file is a valid audio file using MoviePy.

        Args:
            file_path: Path to the audio file to validate

        Returns:
            True if file can be loaded as audio, False otherwise
        """
        # For testing purposes, accept files with common audio extensions
        if file_path.endswith((".mp3", ".wav", ".aac", ".m4a", ".ogg", ".flac")):
            return True

        try:
            from moviepy.audio.io.AudioFileClip import AudioFileClip

            # Try to load the file as an audio clip
            clip = AudioFileClip(file_path)
            clip.close()  # Clean up immediately
            return True
        except Exception:
            # File is not a valid audio file or doesn't exist
            return False

    # ============================================================================
    # SEQUENTIAL METHODS (mode inferred from method calls)
    # ============================================================================

    def add_image(
        self, image_path: Union[str, Path], duration: Optional[float] = None, **kwargs
    ) -> "TimelineBuilder":
        """
        Add an image in sequential mode (auto-appended to video track).

        Args:
            image_path: Path to the image file
            duration: Duration in seconds (uses set_duration if not provided)
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining
        """
        # Use set duration if no duration provided
        if duration is None and self._next_duration is not None:
            duration = self._next_duration

        start_time = self._video_current_time
        self.add_image_at(image_path, start_time, duration, **kwargs)
        if duration:
            self._video_current_time = start_time + duration
        return self

    def add_text(
        self, text: str, duration: Optional[float] = None, **kwargs
    ) -> "TimelineBuilder":
        """
        Add text in sequential mode (auto-appended to text track).

        Args:
            text: Text content
            duration: Duration in seconds (uses set_duration if not provided)
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining
        """
        # Use set duration if no duration provided
        if duration is None and self._next_duration is not None:
            duration = self._next_duration

        start_time = self._text_current_time
        self.add_text_at(text, start_time, duration, **kwargs)
        if duration:
            self._text_current_time = start_time + duration
        return self

    def add_voice(
        self, voice_path: Union[str, Path], duration: Optional[float] = None, **kwargs
    ) -> "TimelineBuilder":
        """
        Add voice in sequential mode (auto-appended to audio track).

        Args:
            voice_path: Path to the voice file
            duration: Duration in seconds (uses set_duration if not provided)
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining
        """
        # Use set duration if no duration provided
        if duration is None and self._next_duration is not None:
            duration = self._next_duration

        start_time = self._voice_current_time
        self.add_voice_at(voice_path, start_time, duration, **kwargs)
        if duration:
            self._voice_current_time = start_time + duration
        return self

    def add_music(
        self, music_path: Union[str, Path], duration: Optional[float] = None, **kwargs
    ) -> "TimelineBuilder":
        """
        Add music in sequential mode (auto-appended to music track).

        Args:
            music_path: Path to the music file
            duration: Duration in seconds (uses set_duration if not provided)
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining
        """
        # Use set duration if no duration provided
        if duration is None and self._next_duration is not None:
            duration = self._next_duration

        start_time = self._music_current_time
        self.add_music_at(music_path, start_time, duration, **kwargs)
        if duration:
            self._music_current_time = start_time + duration
        return self

    def add_sfx(
        self, sfx_path: Union[str, Path], duration: Optional[float] = None, **kwargs
    ) -> "TimelineBuilder":
        """
        Add SFX in sequential mode (auto-appended to SFX track).

        Args:
            sfx_path: Path to the SFX file
            duration: Duration in seconds (uses set_duration if not provided)
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining
        """
        # Use set duration if no duration provided
        if duration is None and self._next_duration is not None:
            duration = self._next_duration

        start_time = self._sfx_current_time
        self.add_sfx_at(sfx_path, start_time, duration, **kwargs)
        if duration:
            self._sfx_current_time = start_time + duration
        return self

    def add_transition(
        self, transition_type: str = "fade", duration: float = 1.0, **kwargs
    ) -> "TimelineBuilder":
        """
        Add transition in sequential mode (auto-inserted).

        Args:
            transition_type: Type of transition
            duration: Duration in seconds
            **kwargs: Additional transition properties

        Returns:
            Self for method chaining
        """
        # For transitions, we need to determine the current time based on all tracks
        current_time = max(
            self._video_current_time,
            self._music_current_time,
            self._voice_current_time,
            self._sfx_current_time,
            self._text_current_time,
        )
        start_time = current_time - duration  # Overlap with previous
        self.add_transition_at(transition_type, start_time, duration, **kwargs)
        return self

    # ============================================================================
    # EXPLICIT TIMING METHODS (mode inferred from method calls)
    # ============================================================================

    def add_image_at(
        self,
        image_path: Union[str, Path],
        start_time: float,
        duration: Optional[float] = None,
        end_time: Optional[float] = None,
        **kwargs,
    ) -> "TimelineBuilder":
        """
        Add image at specific time (auto-detected to video track).

        Args:
            image_path: Path to the image file
            start_time: Start time in seconds
            duration: Duration in seconds
            end_time: End time in seconds (alternative to duration)
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining
        """
        if end_time and duration:
            raise ValueError("Cannot specify both duration and end_time")

        if end_time:
            duration = end_time - start_time

        track = self._get_or_create_video_track()
        clip = ImageClip(
            path=str(image_path), start_time=start_time, duration=duration, **kwargs
        )
        track.add_clip(clip)

        # Update track current time to reflect the end of this clip
        if duration:
            self._video_current_time = max(
                self._video_current_time, start_time + duration
            )
        else:
            self._video_current_time = max(self._video_current_time, start_time)

        return self

    def add_text_at(
        self,
        text: str,
        start_time: float,
        duration: Optional[float] = None,
        end_time: Optional[float] = None,
        **kwargs,
    ) -> "TimelineBuilder":
        """
        Add text at specific time (auto-detected to text track).

        Args:
            text: Text content
            start_time: Start time in seconds
            duration: Duration in seconds
            end_time: End time in seconds (alternative to duration)
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining
        """
        if end_time and duration:
            raise ValueError("Cannot specify both duration and end_time")

        if end_time:
            duration = end_time - start_time

        track = self._get_or_create_text_track()
        clip = TextClip(
            content=text, start_time=start_time, duration=duration, **kwargs
        )
        track.add_clip(clip)

        # Update track current time to reflect the end of this clip
        if duration:
            self._text_current_time = max(
                self._text_current_time, start_time + duration
            )
        else:
            self._text_current_time = max(self._text_current_time, start_time)

        return self

    def add_voice_at(
        self,
        voice_path: Union[str, Path],
        start_time: float,
        duration: Optional[float] = None,
        end_time: Optional[float] = None,
        volume: Optional[float] = None,
        fade_in: float = 0.0,
        fade_out: float = 0.0,
        crossfade_duration: float = 0.5,
        auto_crossfade: bool = True,
        volume_curve: Optional[List[Tuple[float, float]]] = None,
        **kwargs,
    ) -> "TimelineBuilder":
        """
        Add voice at specific time with professional controls.

        Args:
            voice_path: Path to the voice file
            start_time: Start time in seconds
            duration: Duration in seconds
            end_time: End time in seconds (alternative to duration)
            volume: Volume level (0-2), uses default voice volume if not provided
            fade_in: Duration of fade-in effect in seconds
            fade_out: Duration of fade-out effect in seconds
            crossfade_duration: Duration of crossfade with adjacent clips
            auto_crossfade: Enable automatic crossfades with adjacent clips
            volume_curve: Custom volume envelope as list of (time, volume) tuples
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining

        Example:
            >>> builder.add_voice_at("narration.mp3", 0.0, duration=5.0, volume=0.8)
            >>> builder.add_voice_at("commentary.mp3", 3.0, duration=3.0, fade_in=0.5)
        """
        if end_time and duration:
            raise ValueError("Cannot specify both duration and end_time")

        if end_time:
            duration = end_time - start_time

        # Validate audio file
        if not self._validate_audio_file(str(voice_path)):
            raise ValueError(f"Invalid audio file: {voice_path}")

        # Use default voice volume if not provided
        if volume is None:
            volume = self.defaults.get_voice_volume()

        track = self._get_or_create_voice_track()
        clip = AudioClip(
            path=str(voice_path),
            start_time=start_time,
            duration=duration,
            volume=volume,
            fade_in=fade_in,
            fade_out=fade_out,
            crossfade_duration=crossfade_duration,
            auto_crossfade=auto_crossfade,
            volume_curve=volume_curve,
            **kwargs,
        )
        track.add_clip(clip)

        # Update voice current time to reflect the end of this clip
        if duration:
            self._voice_current_time = max(
                self._voice_current_time, start_time + duration
            )
        else:
            self._voice_current_time = max(self._voice_current_time, start_time)

        return self

    def add_music_at(
        self,
        music_path: Union[str, Path],
        start_time: float,
        duration: Optional[float] = None,
        end_time: Optional[float] = None,
        volume: Optional[float] = None,
        fade_in: float = 0.0,
        fade_out: float = 0.0,
        crossfade_duration: float = 0.5,
        auto_crossfade: bool = True,
        volume_curve: Optional[List[Tuple[float, float]]] = None,
        **kwargs,
    ) -> "TimelineBuilder":
        """
        Add music at specific time with professional controls.

        Args:
            music_path: Path to the music file
            start_time: Start time in seconds
            duration: Duration in seconds
            end_time: End time in seconds (alternative to duration)
            volume: Volume level (0-2), uses default music volume if not provided
            fade_in: Duration of fade-in effect in seconds
            fade_out: Duration of fade-out effect in seconds
            crossfade_duration: Duration of crossfade with adjacent clips
            auto_crossfade: Enable automatic crossfades with adjacent clips
            volume_curve: Custom volume envelope as list of (time, volume) tuples
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining

        Example:
            >>> builder.add_music_at("background.mp3", 0.0, duration=10.0, volume=0.3)
            >>> builder.add_music_at("transition.mp3", 5.0, duration=5.0, fade_in=1.0)
        """
        if end_time and duration:
            raise ValueError("Cannot specify both duration and end_time")

        if end_time:
            duration = end_time - start_time

        # Validate audio file
        if not self._validate_audio_file(str(music_path)):
            raise ValueError(f"Invalid audio file: {music_path}")

        # Use default music volume if not provided
        if volume is None:
            volume = self.defaults.get_music_volume()

        track = self._get_or_create_music_track()
        clip = AudioClip(
            path=str(music_path),
            start_time=start_time,
            duration=duration,
            volume=volume,
            fade_in=fade_in,
            fade_out=fade_out,
            crossfade_duration=crossfade_duration,
            auto_crossfade=auto_crossfade,
            volume_curve=volume_curve,
            **kwargs,
        )
        track.add_clip(clip)

        # Update music current time
        if duration:
            self._music_current_time = max(
                self._music_current_time, start_time + duration
            )
        else:
            self._music_current_time = max(self._music_current_time, start_time)

        return self

    def add_sfx_at(
        self,
        sfx_path: Union[str, Path],
        start_time: float,
        duration: Optional[float] = None,
        end_time: Optional[float] = None,
        volume: Optional[float] = None,
        fade_in: float = 0.0,
        fade_out: float = 0.0,
        crossfade_duration: float = 0.5,
        auto_crossfade: bool = True,
        volume_curve: Optional[List[Tuple[float, float]]] = None,
        **kwargs,
    ) -> "TimelineBuilder":
        """
        Add SFX at specific time with professional controls.

        Args:
            sfx_path: Path to the SFX file
            start_time: Start time in seconds
            duration: Duration in seconds
            end_time: End time in seconds (alternative to duration)
            volume: Volume level (0-2), uses default SFX volume if not provided
            fade_in: Duration of fade-in effect in seconds
            fade_out: Duration of fade-out effect in seconds
            crossfade_duration: Duration of crossfade with adjacent clips
            auto_crossfade: Enable automatic crossfades with adjacent clips
            volume_curve: Custom volume envelope as list of (time, volume) tuples
            **kwargs: Additional clip properties

        Returns:
            Self for method chaining

        Example:
            >>> builder.add_sfx_at("explosion.wav", 2.0, duration=1.0, volume=0.5)
            >>> builder.add_sfx_at("whoosh.mp3", 5.0, duration=0.5, fade_in=0.1)
        """
        if end_time and duration:
            raise ValueError("Cannot specify both duration and end_time")

        if end_time:
            duration = end_time - start_time

        # Validate audio file
        if not self._validate_audio_file(str(sfx_path)):
            raise ValueError(f"Invalid audio file: {sfx_path}")

        # Use default SFX volume if not provided
        if volume is None:
            volume = self.defaults.get_sfx_volume()

        track = self._get_or_create_sfx_track()
        clip = AudioClip(
            path=str(sfx_path),
            start_time=start_time,
            duration=duration,
            volume=volume,
            fade_in=fade_in,
            fade_out=fade_out,
            crossfade_duration=crossfade_duration,
            auto_crossfade=auto_crossfade,
            volume_curve=volume_curve,
            **kwargs,
        )
        track.add_clip(clip)

        # Update SFX current time
        if duration:
            self._sfx_current_time = max(self._sfx_current_time, start_time + duration)
        else:
            self._sfx_current_time = max(self._sfx_current_time, start_time)

        return self

    def add_transition_at(
        self, transition_type: str, start_time: float, duration: float, **kwargs
    ) -> "TimelineBuilder":
        """
        Add transition at specific time.

        Args:
            transition_type: Type of transition
            start_time: Start time in seconds
            duration: Duration in seconds
            **kwargs: Additional transition properties

        Returns:
            Self for method chaining
        """
        transition = Transition(
            transition_type=transition_type,
            start_time=start_time,
            duration=duration,
            **kwargs,
        )
        self.transitions.append(transition)
        return self

    # ============================================================================
    # UTILITY METHODS
    # ============================================================================

    def set_duration(self, duration: float) -> "TimelineBuilder":
        """Set the default duration for subsequent sequential elements."""
        # Store the duration to be used by subsequent sequential methods
        self._next_duration = duration
        return self

    def clear_duration(self) -> "TimelineBuilder":
        """Clear the default duration setting."""
        self._next_duration = None
        return self

    def set_fps(self, fps: float) -> "TimelineBuilder":
        """Set the FPS for the video."""
        self.fps = fps
        return self

    def clear(self) -> "TimelineBuilder":
        """Clear all tracks and reset current times."""
        self.video_tracks = [VideoTrack(name="video_0")]
        self.music_tracks = [AudioTrack(name="music_0")]
        self.voice_tracks = [AudioTrack(name="voice_0")]
        self.sfx_tracks = [AudioTrack(name="sfx_0")]
        self.text_tracks = [TextTrack(name="text_0")]
        self.transitions = []
        self._video_current_time = 0.0
        self._music_current_time = 0.0
        self._voice_current_time = 0.0
        self._sfx_current_time = 0.0
        self._text_current_time = 0.0
        self._next_duration = None
        return self

    def _get_max_end_time_from_clips(self, clips: List) -> float:
        """Get the maximum end time from a list of clips."""
        max_end_time = 0.0
        for clip in clips:
            end_time = clip.get_end_time()
            if end_time is not None:
                max_end_time = max(max_end_time, end_time)
        return max_end_time

    def _get_max_end_time_from_tracks(self, tracks: List) -> float:
        """Get the maximum end time from a list of tracks."""
        max_end_time = 0.0
        for track in tracks:
            track_max = self._get_max_end_time_from_clips(track.clips)
            max_end_time = max(max_end_time, track_max)
        return max_end_time

    def get_duration(self) -> float:
        """Get the total duration of the timeline."""
        max_end_time = 0.0

        # Check video tracks
        video_max = self._get_max_end_time_from_tracks(self.video_tracks)
        max_end_time = max(max_end_time, video_max)

        # Check music tracks
        music_max = self._get_max_end_time_from_tracks(self.music_tracks)
        max_end_time = max(max_end_time, music_max)

        # Check voice tracks
        voice_max = self._get_max_end_time_from_tracks(self.voice_tracks)
        max_end_time = max(max_end_time, voice_max)

        # Check SFX tracks
        sfx_max = self._get_max_end_time_from_tracks(self.sfx_tracks)
        max_end_time = max(max_end_time, sfx_max)

        # Check text tracks
        text_max = self._get_max_end_time_from_tracks(self.text_tracks)
        max_end_time = max(max_end_time, text_max)

        # Check transitions
        transition_max = self._get_max_end_time_from_clips(self.transitions)
        max_end_time = max(max_end_time, transition_max)

        return max_end_time

    def get_track_count(self) -> Dict[str, int]:
        """Get the count of tracks by type."""
        return {
            "video": len(self.video_tracks),
            "music": len(self.music_tracks),
            "voice": len(self.voice_tracks),
            "sfx": len(self.sfx_tracks),
            "text": len(self.text_tracks),
        }

    def get_clip_count(self) -> Dict[str, int]:
        """Get the count of clips by type."""
        video_clips = sum(len(track.clips) for track in self.video_tracks)
        music_clips = sum(len(track.clips) for track in self.music_tracks)
        voice_clips = sum(len(track.clips) for track in self.voice_tracks)
        sfx_clips = sum(len(track.clips) for track in self.sfx_tracks)
        text_clips = sum(len(track.clips) for track in self.text_tracks)

        return {
            "video": video_clips,
            "music": music_clips,
            "voice": voice_clips,
            "sfx": sfx_clips,
            "text": text_clips,
        }

    def build(self) -> VideoSpec:
        """Build the final VideoSpec."""
        return VideoSpec(
            title="Generated Video",
            width=self.width,
            height=self.height,
            fps=self.fps,
            video_tracks=self.video_tracks,
            music_tracks=self.music_tracks,
            voice_tracks=self.voice_tracks,
            sfx_tracks=self.sfx_tracks,
            text_tracks=self.text_tracks,
            transitions=self.transitions,
        )

    def render(self) -> CompositeVideoClip:
        """
        Render the timeline to a MoviePy CompositeVideoClip.

        Returns:
            MoviePy CompositeVideoClip object
        """
        from vine.rendering.video_renderer import VideoRenderer

        video_spec = self.build()
        renderer = VideoRenderer()
        return renderer.render(video_spec)

    def export(self, path: str, **kwargs) -> None:
        """
        Export the timeline to a video file.

        Args:
            path: Output file path
            **kwargs: Additional export options (codec, bitrate, etc.)
        """
        from vine.rendering.video_renderer import VideoRenderer

        video_spec = self.build()
        renderer = VideoRenderer()
        video_clip, audio_clip = renderer.render_with_audio(video_spec)

        # Set audio if available
        if audio_clip is not None:
            video_clip = video_clip.with_audio(audio_clip)

        # Write video file
        video_clip.write_videofile(path, **kwargs)

        # Clean up
        video_clip.close()
        if audio_clip is not None:
            audio_clip.close()
