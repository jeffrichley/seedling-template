Contributing to Project Vine
============================

Thank you for your interest in contributing to Project Vine! This document provides guidelines and requirements for contributing to the project.

.. contents:: Table of Contents
   :local:

Code of Conduct
---------------

By participating in this project, you agree to maintain a respectful environment for everyone. We are committed to providing a welcoming and inspiring community for all.

Development Setup
----------------

Prerequisites
~~~~~~~~~~~~

- **Python 3.11+**: Required for modern type hints and features
- **uv**: Fast Python package manager (recommended)
- **Git**: Version control system

Installation
~~~~~~~~~~~

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/jeffrichley/vine.git
   cd vine

   # Install with uv (recommended)
   uv sync

   # Or install with pip
   pip install -r requirements.txt

   # Install in editable mode for development
   uv pip install -e ".[dev,docs]"

Development Environment
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Activate virtual environment
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate     # On Windows

   # Verify installation
   uv run dev info

Quality Requirements
-------------------

Project Vine maintains strict quality standards. **All contributions must pass these quality gates:**

Quality Gates
~~~~~~~~~~~~

1. **🔍 Linting (Ruff)**: Code style and best practices
2. **🧠 Type Safety (MyPy)**: Strict type checking with zero errors
3. **📊 Coverage (≥80%)**: Comprehensive test coverage
4. **📈 Complexity (Xenon)**: Maintainable code complexity
5. **🧹 Dead Code (Vulture)**: No unused code or imports
6. **🔒 Security (pip-audit)**: No dependency vulnerabilities
7. **📚 Documentation (Interrogate)**: 50%+ docstring coverage

Pre-commit Checks
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run all quality checks
   uv run dev checkit

   # Individual checks
   uv run dev lint          # Ruff linting
   uv run dev typecheck     # MyPy type checking
   uv run dev test          # Pytest with coverage
   uv run dev quality-gates # All quality gates

Contribution Process
-------------------

1. Fork and Clone
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Fork the repository on GitHub
   # Clone your fork
   git clone https://github.com/YOUR_USERNAME/vine.git
   cd vine

   # Add upstream remote
   git remote add upstream https://github.com/jeffrichley/vine.git

2. Create a Feature Branch
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Create and switch to a new branch
   git checkout -b feature/your-feature-name

   # Or for bug fixes
   git checkout -b fix/your-bug-description

3. Make Your Changes
~~~~~~~~~~~~~~~~~~~

- Follow the Code Style Guidelines
- Write comprehensive tests
- Update documentation as needed
- Ensure all quality gates pass

4. Test Your Changes
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run all tests
   uv run dev test

   # Run quality gates
   uv run dev quality-gates

   # Run benchmarks (if applicable)
   uv run dev benchmark

5. Commit Your Changes
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Stage your changes
   git add .

   # Commit with a descriptive message
   git commit -m "feat: add new video transition effect

   - Implement crossfade transition
   - Add comprehensive tests
   - Update documentation
   - Fixes #123"

6. Push and Create Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Push to your fork
   git push origin feature/your-feature-name

   # Create a Pull Request on GitHub

Code Style Guidelines
--------------------

Python Code Style
~~~~~~~~~~~~~~~~

- **Black**: Automatic code formatting (line length: 88)
- **Ruff**: Linting and import sorting
- **Type Hints**: Required for all functions and methods
- **Docstrings**: Google-style docstrings for all public APIs

Import Organization
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Standard library imports
   import os
   import sys
   from typing import List, Optional

   # Third-party imports
   import numpy as np
   import pydantic

   # Local imports
   from vine.models import VideoSpec
   from vine.rendering import VideoRenderer

Type Annotations
~~~~~~~~~~~~~~~

.. code-block:: python

   # Required for all functions
   def process_video(spec: VideoSpec, output_path: str) -> bool:
       """Process a video specification and save to output path.

       Args:
           spec: The video specification to process
           output_path: Path where the video will be saved

       Returns:
           True if processing was successful, False otherwise
       """
       pass

Error Handling
~~~~~~~~~~~~~

.. code-block:: python

   # Use specific exceptions
   try:
       result = process_data(data)
   except ValueError as e:
       logger.error(f"Invalid data format: {e}")
       raise
   except FileNotFoundError as e:
       logger.error(f"Required file not found: {e}")
       raise

Testing Requirements
-------------------

Test Coverage
~~~~~~~~~~~~

- **Minimum Coverage**: 80% overall
- **New Code**: 100% coverage required
- **Critical Paths**: 100% coverage required

Test Structure
~~~~~~~~~~~~~

.. code-block:: python

   # tests/unit/test_video_spec.py
   import pytest
   from vine.models import VideoSpec

   class TestVideoSpec:
       def test_video_spec_creation(self):
           """Test VideoSpec creation with valid parameters."""
           spec = VideoSpec(
               width=1920,
               height=1080,
               duration=10.0
           )
           assert spec.width == 1920
           assert spec.height == 1080
           assert spec.duration == 10.0

       def test_video_spec_validation(self):
           """Test VideoSpec validation with invalid parameters."""
           with pytest.raises(ValueError):
               VideoSpec(width=-1, height=1080, duration=10.0)

Property-Based Testing
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use Hypothesis for property-based testing
   from hypothesis import given, strategies as st

   @given(st.integers(min_value=1, max_value=3840))
   def test_video_width_validation(width):
       """Test that video width validation works for all valid values."""
       spec = VideoSpec(width=width, height=1080, duration=10.0)
       assert spec.width == width

Documentation Standards
----------------------

Docstring Requirements
~~~~~~~~~~~~~~~~~~~~~

- **All public APIs**: Must have Google-style docstrings
- **Parameters**: Document all parameters with types
- **Returns**: Document return values and types
- **Examples**: Include usage examples for complex functions

Example Docstring
~~~~~~~~~~~~~~~~

.. code-block:: python

   def create_video_timeline(
       clips: List[VideoClip],
       transitions: Optional[List[Transition]] = None,
       duration: Optional[float] = None
   ) -> VideoTimeline:
       """Create a video timeline from a list of clips.

       Args:
           clips: List of video clips to include in the timeline
           transitions: Optional list of transitions between clips
           duration: Optional total duration (auto-calculated if None)

       Returns:
           A VideoTimeline object representing the composed video

       Raises:
           ValueError: If clips list is empty or invalid
           TypeError: If clips contain invalid types

       Example:
           >>> clips = [VideoClip("video1.mp4"), VideoClip("video2.mp4")]
           >>> timeline = create_video_timeline(clips)
           >>> timeline.render("output.mp4")
       """
       pass

README Updates
~~~~~~~~~~~~~

- Update README.md for user-facing changes
- Update API documentation for technical changes
- Include examples for new features

Review Process
-------------

Pull Request Requirements
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Quality Gates**: All quality gates must pass
2. **Tests**: All tests must pass
3. **Documentation**: Updated as needed
4. **Description**: Clear description of changes
5. **Linked Issues**: Reference related issues

Review Checklist
~~~~~~~~~~~~~~~

- [ ] Code follows style guidelines
- [ ] Type hints are complete and correct
- [ ] Tests are comprehensive and pass
- [ ] Documentation is updated
- [ ] No breaking changes (or properly documented)
- [ ] Performance impact considered
- [ ] Security implications reviewed

Review Timeline
~~~~~~~~~~~~~~

- **Initial Review**: Within 48 hours
- **Follow-up Reviews**: Within 24 hours
- **Merge**: After approval and CI passes

Getting Help
-----------

Questions and Discussions
~~~~~~~~~~~~~~~~~~~~~~~~~

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Documentation**: Check the docs/ directory for detailed guides

Development Resources
~~~~~~~~~~~~~~~~~~~~

- **API Documentation**: `docs/api/`
- **Architecture Guide**: `docs/ARCHITECTURE_PATTERNS.md`
- **Quality Gates**: `docs/QUALITY_GATES.md`
- **Project Status**: `docs/STATUS.md`

Recognition
----------

Contributors will be recognized in:

- **README.md**: For significant contributions
- **CHANGELOG.md**: For all contributions
- **GitHub Contributors**: Automatic recognition

Thank you for contributing to Project Vine! 🎬
