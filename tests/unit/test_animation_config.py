"""Unit tests for AnimationConfig model."""

import pytest

from vine.models import AnimationConfig, KenBurnsConfig


class TestAnimationConfig:
    """Test AnimationConfig model."""

    def test_create_ken_burns_animation(self):
        """Test creating a Ken Burns animation."""
        ken_burns = KenBurnsConfig(zoom_factor=1.5, pan_x=0.2, pan_y=-0.1)

        animation = AnimationConfig(effect=ken_burns, start_time=0.0, duration=3.0)

        assert animation.effect.type == "ken_burns"
        assert animation.effect.zoom_factor == 1.5
        assert animation.start_time == 0.0
        assert animation.duration == 3.0
        assert animation.get_end_time() == 3.0

    def test_animation_validation(self):
        """Test animation validation."""
        ken_burns = KenBurnsConfig()

        # Test invalid start time
        with pytest.raises(
            ValueError, match="Input should be greater than or equal to 0"
        ):
            AnimationConfig(effect=ken_burns, start_time=-1.0)

        # Test invalid easing
        with pytest.raises(ValueError, match="Unsupported easing function"):
            AnimationConfig(effect=ken_burns, easing="invalid_easing")

    def test_validate_easing_success(self):
        """Test validate_easing method returns valid easing values unchanged."""
        ken_burns = KenBurnsConfig()

        # Test all valid easing values are returned unchanged
        valid_easings = [
            "linear",
            "ease_in",
            "ease_out",
            "ease_in_out",
            "ease_in_quad",
            "ease_out_quad",
            "ease_in_out_quad",
            "ease_in_cubic",
            "ease_out_cubic",
            "ease_in_out_cubic",
        ]

        for easing in valid_easings:
            animation = AnimationConfig(effect=ken_burns, easing=easing)
            assert animation.easing == easing

    def test_animation_methods(self):
        """Test AnimationConfig methods."""
        ken_burns = KenBurnsConfig()
        animation = AnimationConfig(effect=ken_burns, start_time=1.0, duration=2.0)

        # Test get_end_time
        assert animation.get_end_time() == 3.0

        # Test overlaps_with
        other_anim = AnimationConfig(effect=ken_burns, start_time=2.0, duration=2.0)
        assert animation.overlaps_with(other_anim) is True

        non_overlapping = AnimationConfig(
            effect=ken_burns, start_time=4.0, duration=2.0
        )
        assert animation.overlaps_with(non_overlapping) is False

    def test_animation_without_duration(self):
        """Test animation without duration."""
        ken_burns = KenBurnsConfig()
        animation = AnimationConfig(effect=ken_burns, start_time=1.0)

        assert animation.get_end_time() is None
        assert (
            animation.overlaps_with(animation) is False
        )  # Can't overlap without duration

    def test_animation_overlap_without_duration(self):
        """Test animation overlap when one or both animations have no duration."""
        ken_burns = KenBurnsConfig()
        anim1 = AnimationConfig(effect=ken_burns, start_time=0.0, duration=2.0)
        anim2 = AnimationConfig(effect=ken_burns, start_time=1.0)  # No duration

        # Should return False when either animation has no duration
        assert anim1.overlaps_with(anim2) is False
        assert anim2.overlaps_with(anim1) is False
