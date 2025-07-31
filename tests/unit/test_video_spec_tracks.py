"""Unit tests for track-based VideoSpec model."""

import pytest

from vine.models import (
    AudioClip,
    AudioTrack,
    MusicConfig,
    TextClip,
    TextTrack,
    Transition,
    VideoClip,
    VideoSpec,
    VideoTrack,
    VoiceConfig,
)
from vine.models.tracks import TrackType
from vine.models.transition import TransitionType


class TestVideoSpecTracks:
    """Test track-based VideoSpec model."""

    def test_create_basic_video_spec(self) -> None:
        """Test creating a basic video specification."""
        spec = VideoSpec(
            title="Test Video", description="A test video", width=1920, height=1080
        )
        assert spec.title == "Test Video"
        assert spec.description == "A test video"
        assert spec.width == 1920
        assert spec.height == 1080
        assert spec.fps == 30.0
        assert spec.output_format == "mp4"
        assert spec.quality == "high"

    def test_video_spec_validation(self) -> None:
        """Test video specification validation."""
        # Test invalid width
        with pytest.raises(
            ValueError, match="Input should be greater than or equal to 1"
        ):
            VideoSpec(title="Test", width=0)
        # Test invalid height
        with pytest.raises(
            ValueError, match="Input should be greater than or equal to 1"
        ):
            VideoSpec(title="Test", height=0)
        # Test invalid FPS
        with pytest.raises(
            ValueError, match="Input should be greater than or equal to 1"
        ):
            VideoSpec(title="Test", fps=0.5)
        # Test invalid background color
        with pytest.raises(ValueError, match="String should match pattern"):
            VideoSpec(title="Test", background_color="invalid")

    def test_background_color_validation(self) -> None:
        """Test background color validation."""
        # Test valid hex colors
        valid_colors = [
            "#000000",
            "#FFFFFF",
            "#FF0000",
            "#00FF00",
            "#0000FF",
            "#123456",
        ]
        for color in valid_colors:
            spec = VideoSpec(title="Test", background_color=color)
            assert spec.background_color == color
        # Test invalid hex colors - missing #
        with pytest.raises(ValueError, match="String should match pattern"):
            VideoSpec(title="Test", background_color="000000")
        # Test invalid hex colors - wrong length
        with pytest.raises(ValueError, match="String should match pattern"):
            VideoSpec(title="Test", background_color="#00000")  # Too short
        with pytest.raises(ValueError, match="String should match pattern"):
            VideoSpec(title="Test", background_color="#0000000")  # Too long

    def test_video_spec_dimension_limits(self) -> None:
        """Test video specification dimension limits."""
        # Test maximum dimensions
        spec = VideoSpec(title="Test", width=7680, height=7680)
        assert spec.width == 7680
        assert spec.height == 7680
        # Test minimum dimensions
        spec = VideoSpec(title="Test", width=1, height=1)
        assert spec.width == 1
        assert spec.height == 1

    def test_video_spec_methods(self) -> None:
        """Test VideoSpec methods."""
        spec = VideoSpec(title="Test Video")
        # Test get_total_duration with empty tracks
        assert spec.get_total_duration() == 0.0
        # Test get_active_clips_at_time with empty tracks
        active_clips = spec.get_active_clips_at_time(0.0)
        assert active_clips["video"] == []
        assert active_clips["music"] == []
        assert active_clips["voice"] == []
        assert active_clips["sfx"] == []
        assert active_clips["text"] == []
        # Test get_transitions_at_time with empty transitions
        transitions = spec.get_transitions_at_time(0.0)
        assert transitions == []

    def test_video_spec_track_management(self) -> None:
        """Test VideoSpec track management."""
        spec = VideoSpec(title="Test Video")
        # Test adding tracks
        video_track = VideoTrack(name="video_1")
        music_track = AudioTrack(name="music_1")
        voice_track = AudioTrack(name="voice_1")
        sfx_track = AudioTrack(name="sfx_1")
        text_track = TextTrack(name="text_1")
        spec.add_video_track(video_track)
        spec.add_music_track(music_track)
        spec.add_voice_track(voice_track)
        spec.add_sfx_track(sfx_track)
        spec.add_text_track(text_track)
        assert len(spec.video_tracks) == 2  # Default + added
        assert len(spec.music_tracks) == 2  # Default + added
        assert len(spec.voice_tracks) == 2  # Default + added
        assert len(spec.sfx_tracks) == 2  # Default + added
        assert len(spec.text_tracks) == 2  # Default + added
        # Test getting track by name
        found_video = spec.get_track_by_name("video_1", TrackType.VIDEO)
        assert found_video is not None
        assert found_video.name == "video_1"
        found_music = spec.get_track_by_name("music_1", TrackType.MUSIC)
        assert found_music is not None
        assert found_music.name == "music_1"
        found_voice = spec.get_track_by_name("voice_1", TrackType.VOICE)
        assert found_voice is not None
        assert found_voice.name == "voice_1"
        found_sfx = spec.get_track_by_name("sfx_1", TrackType.SFX)
        assert found_sfx is not None
        assert found_sfx.name == "sfx_1"
        found_text = spec.get_track_by_name("text_1", TrackType.TEXT)
        assert found_text is not None
        assert found_text.name == "text_1"
        # Test removing tracks
        assert spec.remove_track("video_1", TrackType.VIDEO)
        assert spec.remove_track("music_1", TrackType.MUSIC)
        assert spec.remove_track("voice_1", TrackType.VOICE)
        assert spec.remove_track("sfx_1", TrackType.SFX)
        assert spec.remove_track("text_1", TrackType.TEXT)
        assert len(spec.video_tracks) == 1  # Only default
        assert len(spec.music_tracks) == 1  # Only default
        assert len(spec.voice_tracks) == 1  # Only default
        assert len(spec.sfx_tracks) == 1  # Only default
        assert len(spec.text_tracks) == 1  # Only default

    def test_get_track_by_name_edge_cases(self) -> None:
        """Test get_track_by_name method edge cases that return None."""
        spec = VideoSpec(title="Test Video")
        # Test getting non-existent video track
        result = spec.get_track_by_name("non_existent", TrackType.VIDEO)
        assert result is None
        # Test getting non-existent music track
        result = spec.get_track_by_name("non_existent", TrackType.MUSIC)
        assert result is None
        # Test getting non-existent voice track
        result = spec.get_track_by_name("non_existent", TrackType.VOICE)
        assert result is None
        # Test getting non-existent sfx track
        result = spec.get_track_by_name("non_existent", TrackType.SFX)
        assert result is None
        # Test getting non-existent text track
        result = spec.get_track_by_name("non_existent", TrackType.TEXT)
        assert result is None
        # Test with empty string track name
        result = spec.get_track_by_name("", TrackType.VIDEO)
        assert result is None
        # Test with None track name (should return None gracefully)
        result = spec.get_track_by_name(
            None, TrackType.VIDEO
        )  # intentional invalid input for testing
        assert result is None

    def test_remove_track_edge_cases(self) -> None:
        """Test remove_track method edge cases that return False."""
        spec = VideoSpec(title="Test Video")
        # Test removing non-existent video track
        result = spec.remove_track("non_existent", TrackType.VIDEO)
        assert result is False
        # Test removing non-existent music track
        result = spec.remove_track("non_existent", TrackType.MUSIC)
        assert result is False
        # Test removing non-existent voice track
        result = spec.remove_track("non_existent", TrackType.VOICE)
        assert result is False
        # Test removing non-existent sfx track
        result = spec.remove_track("non_existent", TrackType.SFX)
        assert result is False
        # Test removing non-existent text track
        result = spec.remove_track("non_existent", TrackType.TEXT)
        assert result is False
        # Test with empty string track name
        result = spec.remove_track("", TrackType.VIDEO)
        assert result is False
        # Test with None track name (should return False gracefully)
        result = spec.remove_track(
            None, TrackType.VIDEO
        )  # intentional invalid input for testing
        assert result is False
        # Test removing default tracks (should succeed since there's no protection)
        result = spec.remove_track("video_0", TrackType.VIDEO)
        assert result is True
        result = spec.remove_track("music_0", TrackType.MUSIC)
        assert result is True
        result = spec.remove_track("voice_0", TrackType.VOICE)
        assert result is True
        result = spec.remove_track("sfx_0", TrackType.SFX)
        assert result is True
        result = spec.remove_track("text_0", TrackType.TEXT)
        assert result is True

    def test_video_spec_transition_management(self) -> None:
        """Test VideoSpec transition management."""
        spec = VideoSpec(title="Test Video")
        # Test adding transitions
        transition = Transition(
            transition_type=TransitionType.FADE, start_time=0.0, duration=1.0
        )
        spec.add_transition(transition)
        assert len(spec.transitions) == 1
        # Test removing transitions
        assert spec.remove_transition(0)
        assert len(spec.transitions) == 0
        # Test removing non-existent transition
        assert not spec.remove_transition(0)

    def test_video_spec_time_queries(self) -> None:
        """Test VideoSpec time queries."""
        spec = VideoSpec(title="Test Video")
        # Add some clips to tracks
        video_track = spec.video_tracks[0]
        voice_track = spec.voice_tracks[0]
        text_track = spec.text_tracks[0]
        video_clip = VideoClip(path="video.mp4", start_time=0.0, duration=5.0)
        voice_clip = AudioClip(path="voice.mp3", start_time=1.0, duration=3.0)
        text_clip = TextClip(content="Hello", start_time=2.0, duration=2.0)
        video_track.add_clip(video_clip)
        voice_track.add_clip(voice_clip)
        text_track.add_clip(text_clip)
        # Test get_active_clips_at_time
        active_clips = spec.get_active_clips_at_time(1.5)
        assert len(active_clips["video"]) == 1
        assert len(active_clips["voice"]) == 1
        assert len(active_clips["text"]) == 0  # Text starts at 2.0
        active_clips = spec.get_active_clips_at_time(2.5)
        assert len(active_clips["video"]) == 1
        assert len(active_clips["voice"]) == 1
        assert len(active_clips["text"]) == 1
        # Test get_total_duration
        total_duration = spec.get_total_duration()
        assert total_duration == 5.0  # Video clip ends at 5.0

    def test_video_spec_transitions(self) -> None:
        """Test VideoSpec transitions."""
        spec = VideoSpec(title="Test Video")
        # Add transitions
        transition1 = Transition(
            transition_type=TransitionType.FADE, start_time=0.0, duration=1.0
        )
        transition2 = Transition(
            transition_type=TransitionType.CROSSFADE, start_time=5.0, duration=2.0
        )
        spec.add_transition(transition1)
        spec.add_transition(transition2)
        # Test get_transitions_at_time
        transitions = spec.get_transitions_at_time(0.5)
        assert len(transitions) == 1
        assert transitions[0].transition_type == "fade"
        transitions = spec.get_transitions_at_time(6.0)
        assert len(transitions) == 1
        assert transitions[0].transition_type == "crossfade"
        transitions = spec.get_transitions_at_time(10.0)
        assert transitions == []

    def test_video_spec_z_order_sorting(self) -> None:
        """Test VideoSpec z_order sorting."""
        spec = VideoSpec(title="Test Video")
        # Add tracks with different z_orders
        track1 = VideoTrack(name="video_1", z_order=10)
        track2 = VideoTrack(name="video_2", z_order=5)
        track3 = VideoTrack(name="video_3", z_order=15)
        spec.add_video_track(track1)
        spec.add_video_track(track2)
        spec.add_video_track(track3)
        # The validate_video_configuration method should sort by z_order
        # Default track has z_order=0, so order should be: default, track2, track1, track3
        assert spec.video_tracks[0].name == "video_0"  # Default track
        assert spec.video_tracks[1].name == "video_2"  # z_order=5
        assert spec.video_tracks[2].name == "video_1"  # z_order=10
        assert spec.video_tracks[3].name == "video_3"  # z_order=15

    def test_video_spec_with_voice_and_music_config(self) -> None:
        """Test VideoSpec with voice and music configuration."""
        voice_config = VoiceConfig(volume=0.8, speed=1.2)
        music_config = MusicConfig(volume=0.6, loop=True)
        spec = VideoSpec(
            title="Test Video", voice_config=voice_config, music_config=music_config
        )
        assert spec.voice_config is not None
        assert spec.voice_config.volume == 0.8
        assert spec.voice_config.speed == 1.2
        assert spec.music_config is not None
        assert spec.music_config.volume == 0.6
        assert spec.music_config.loop is True

    def test_get_total_duration_with_transitions(self) -> None:
        """Test get_total_duration method specifically with transitions to exercise lines 101-102."""
        spec = VideoSpec(title="Test Video")
        # Initially, no transitions, so duration should be 0
        assert spec.get_total_duration() == 0.0
        # Add a transition that ends at 5.0 seconds
        transition1 = Transition(
            transition_type=TransitionType.FADE, start_time=0.0, duration=5.0
        )
        spec.add_transition(transition1)
        # Now duration should be 5.0 (from transition)
        assert spec.get_total_duration() == 5.0
        # Add another transition that ends at 8.0 seconds
        transition2 = Transition(
            transition_type=TransitionType.CROSSFADE,
            start_time=3.0,
            duration=5.0,  # ends at 8.0
        )
        spec.add_transition(transition2)
        # Now duration should be 8.0 (max of both transitions)
        assert spec.get_total_duration() == 8.0
        # Add a transition that ends at 10.0 seconds
        transition3 = Transition(
            transition_type=TransitionType.SLIDE,
            start_time=8.0,
            duration=2.0,  # ends at 10.0
        )
        spec.add_transition(transition3)
        # Now duration should be 10.0 (max of all transitions)
        assert spec.get_total_duration() == 10.0
        # Test with zero duration transition
        transition4 = Transition(
            transition_type=TransitionType.DISSOLVE,
            start_time=15.0,
            duration=0.0,  # ends at 15.0
        )
        spec.add_transition(transition4)
        # Duration should still be 15.0 (max of all transitions)
        assert spec.get_total_duration() == 15.0
        # Test that transitions are properly processed in the loop
        # This specifically exercises lines 101-102 in get_total_duration
        for transition in spec.transitions:
            end_time = transition.get_end_time()
            assert end_time == transition.start_time + transition.duration
