# German Tutor - Development Setup & Progress Tracker

## Project Structure

```
german-tutor/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # FastAPI app entry point
│   │   ├── routers/        # API endpoints
│   │   ├── services/       # AI service integrations
│   │   ├── database/       # SQLite models and operations
│   │   ├── config/         # Configuration management
│   │   └── models/         # Pydantic data models
│   ├── requirements.txt
│   └── Dockerfile          # For distribution only
├── frontend/               # React + TypeScript frontend (Vite)
│   ├── src/
│   │   ├── components/     # React components (.tsx)
│   │   ├── services/       # API client (typed)
│   │   ├── types/          # TypeScript type definitions
│   │   └── utils/         # Utilities
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── public/
├── models/                 # Local AI models
├── docs/                   # Documentation
├── tests/                  # Test files and fixtures
├── .env.example            # Environment variables template
├── docker-compose.yml      # For distribution
└── README.md
```

---

## Environment Setup

### Prerequisites
- [ ] macOS with Homebrew installed
- [ ] Python 3.9+ (check with `python3 --version`)
- [ ] Node.js 18+ (check with `node --version`)
- [ ] Git configured

### Phase 1: AI Foundation Setup

#### Install Ollama
- [ ] Install Ollama: `brew install ollama`
- [ ] Start Ollama service: `ollama serve` (run in background)
- [ ] Test download small model first: `ollama pull llama3.2:1b`
- [ ] Verify installation: `ollama list`

#### Install German Models (Phase 1: Testing)
- [ ] Download SmolLM2-German for testing: `ollama pull smollm2-german:360m`
- [ ] Test basic German conversation: `ollama run smollm2-german:360m`
- [ ] Note: OpenEuroLLM-German (7B) installation planned for later

#### Install Python Dependencies
- [ ] Create virtual environment: `python3 -m venv venv`
- [ ] Activate environment: `source venv/bin/activate`
- [ ] Create initial requirements.txt:
```
fastapi
uvicorn
python-multipart
openai-whisper
TTS
requests
pydantic
mypy
pytest>=7.0.0
pytest-asyncio
pytest-mock
sqlalchemy
aiosqlite
python-dotenv
pydub
filetype
```
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Set up mypy for type checking: `mypy --install-types`

#### Test Whisper Installation
- [ ] Test Whisper: `python3 -c "import whisper; print('Whisper installed successfully')"`
- [ ] Download German-optimized model: `whisper --model large-v3-turbo --language German <test_audio.wav>`

#### Backend Project Setup
- [ ] Create backend directory structure (see above)
- [ ] Create `.env.example` file with configuration template
- [ ] Initialize FastAPI app in `backend/app/main.py`
- [ ] Set up SQLite database connection
- [ ] Create basic health check endpoint
- [ ] Test server: `uvicorn app.main:app --reload`
- [ ] Verify at http://localhost:8000/docs

#### Configuration Setup
- [ ] Copy `.env.example` to `.env`: `cp .env.example .env` 
- [ ] Create application data directory: `mkdir -p ~/.german-tutor/{audio,models}`
- [ ] Test configuration loading in FastAPI app
- [ ] Verify database initialization and model selection logic

---

## Phase-by-Phase Progress Tracker

### Phase 1: AI Foundation Setup (Days 1-3) ✅ ❌ 🔄
**Learning Goals:** Local AI ecosystem, model management

- [ ] **Day 1:** Ollama installation and basic model testing
  - [ ] Install Ollama and SmolLM2-German
  - [ ] Test basic German responses
  - [ ] Document model performance on M2
  
- [ ] **Day 2:** FastAPI setup and LLM integration
  - [ ] Create FastAPI project structure with Pydantic models
  - [ ] Set up SQLite database with SQLAlchemy
  - [ ] Create configuration management system (.env file)
  - [ ] Build typed chat endpoint with Ollama integration
  - [ ] Add Python type hints to all functions
  - [ ] Test API with Postman/curl and verify auto-generated docs
  
- [ ] **Day 3:** Model evaluation and optimization
  - [ ] Test OpenEuroLLM-German (7B) if RAM allows
  - [ ] Compare model performance and response quality
  - [ ] Finalize model choice for MVP

**Completion Criteria:** ✅ Working FastAPI endpoint that accepts German text and returns AI responses

---

### Phase 2: Speech Processing Pipeline (Days 4-6) ✅ ❌ 🔄
**Learning Goals:** Audio processing, STT/TTS integration

- [ ] **Day 4:** Whisper STT integration
  - [ ] Add audio file upload endpoint
  - [ ] Integrate Whisper for German speech-to-text
  - [ ] Test with sample German audio files
  
- [ ] **Day 5:** Coqui TTS setup
  - [ ] Install Coqui TTS with German Thorsten voice
  - [ ] Create text-to-speech endpoint
  - [ ] Test German audio output quality
  
- [ ] **Day 6:** Complete pipeline integration
  - [ ] Create combined STT → LLM → TTS endpoint
  - [ ] Test full voice conversation pipeline
  - [ ] Optimize response times

**Completion Criteria:** ✅ Working API endpoint that accepts German audio and returns German audio response

---

### Phase 3: Frontend Integration (Days 7-10) ✅ ❌ 🔄
**Learning Goals:** AI-powered UI, real-time audio

- [ ] **Day 7:** React + TypeScript app setup
  - [ ] Create Vite React app: `npm create vite@latest frontend -- --template react-ts`
  - [ ] Install dependencies: `cd frontend && npm install`
  - [ ] Configure Vite for audio file handling and API proxy
  - [ ] Create typed interfaces for API responses
  - [ ] Set up audio recording capabilities with proper typing
  
- [ ] **Day 8:** API integration
  - [ ] Build API client for backend endpoints
  - [ ] Create chat interface with message history
  - [ ] Add loading states for AI processing
  
- [ ] **Day 9:** Audio handling
  - [ ] Implement audio recording and playback
  - [ ] Connect audio recording to STT endpoint
  - [ ] Add audio response playback
  
- [ ] **Day 10:** UI polish and testing
  - [ ] Add conversation history display
  - [ ] Implement voice controls (start/stop/replay)
  - [ ] Test complete user flow

**Completion Criteria:** ✅ Working React app with voice conversation capabilities

---

### Phase 4: Intelligent Tutoring Features (Days 11-14) ✅ ❌ 🔄
**Learning Goals:** Advanced AI features, prompt engineering

- [ ] **Day 11:** Adaptive difficulty system design
  - [ ] Research German proficiency levels (A1-C2)
  - [ ] Design difficulty assessment logic
  - [ ] Create prompt templates for different levels
  
- [ ] **Day 12:** Learning context management
  - [ ] Implement conversation history storage
  - [ ] Add user progress tracking
  - [ ] Create vocabulary and grammar tracking
  
- [ ] **Day 13:** Feedback features
  - [ ] Add grammar correction suggestions
  - [ ] Implement vocabulary building features
  - [ ] Create learning insights display
  
- [ ] **Day 14:** System integration and testing
  - [ ] Integrate all tutoring features
  - [ ] Test adaptive difficulty progression
  - [ ] Validate learning feedback accuracy

**Completion Criteria:** ✅ App adapts difficulty based on user responses and provides meaningful learning feedback

---

### Phase 5: Production & Distribution (Days 15-21) ✅ ❌ 🔄
**Learning Goals:** AI deployment, performance optimization, distribution

- [ ] **Day 15-16:** Performance optimization
  - [ ] Profile and optimize response times
  - [ ] Implement caching where appropriate
  - [ ] Add comprehensive error handling
  
- [ ] **Day 17-18:** Docker distribution setup
  - [ ] Create production Dockerfiles
  - [ ] Set up docker-compose for easy deployment
  - [ ] Test Docker distribution on different machines
  
- [ ] **Day 19-20:** Documentation and testing
  - [ ] Write comprehensive README
  - [ ] Create setup instructions for classmates
  - [ ] Test installation on fresh systems
  
- [ ] **Day 21:** Demo and portfolio prep
  - [ ] Create demo video
  - [ ] Write technical blog post outline
  - [ ] Prepare portfolio documentation

**Completion Criteria:** ✅ Working Docker distribution with complete documentation

---

## Development Workflow

### Daily Development Process
1. **Start development session**
   - [ ] Activate Python venv: `source venv/bin/activate`
   - [ ] Start Ollama service: `ollama serve` (background)
   - [ ] Start backend: `cd backend && uvicorn app.main:app --reload`
   - [ ] Start frontend: `cd frontend && npm run dev`

2. **Testing checklist**
   - [ ] Run quick smoke tests: `pytest backend/tests/ -v`
   - [ ] Run frontend tests: `cd frontend && npm run test`
   - [ ] Run type checking: `mypy backend/` and `npm run type-check`
   - [ ] Test basic voice pipeline: record → process → playback
   - [ ] Test API endpoints with curl/Postman
   - [ ] Verify AI model responses and type safety
   - [ ] Check audio processing pipeline
   - [ ] Test frontend functionality with TypeScript compilation

3. **End of session**
   - [ ] Commit changes with descriptive messages
   - [ ] Update progress checkboxes above
   - [ ] Note any issues or blockers

### Troubleshooting Common Issues
- [ ] **Ollama not starting:** Check if port 11434 is available
- [ ] **Whisper out of memory:** Use smaller model variant
- [ ] **TTS slow performance:** Check if using GPU acceleration
- [ ] **Frontend API calls failing:** Verify CORS configuration

### Performance Targets
- [ ] STT processing: < 2 seconds for 10-second audio
- [ ] LLM response generation: < 3 seconds
- [ ] TTS generation: < 2 seconds
- [ ] Total conversation round-trip: < 7 seconds

---

## Testing Strategy

### Testing Framework Setup

**Backend Testing (Python)**
- [ ] Install pytest: `pip install pytest pytest-asyncio pytest-mock`
- [ ] Add to requirements.txt: `pytest>=7.0.0, pytest-asyncio, pytest-mock`
- [ ] Create `backend/tests/` directory structure:
  ```
  backend/tests/
  ├── __init__.py
  ├── test_api_endpoints.py
  ├── test_ai_services.py
  ├── test_audio_processing.py
  └── conftest.py
  ```

**Frontend Testing (TypeScript/React)**
- [ ] Install testing libs: `npm install --save-dev vitest @testing-library/react @testing-library/jest-dom @testing-library/user-event`
- [ ] Configure Vitest in `vite.config.ts`
- [ ] Create `frontend/src/tests/` directory
- [ ] Set up test utilities for audio mocking

### Unit Testing Strategy

**Backend Unit Tests**
- [ ] **API Endpoints**: Test request/response schemas, validation, error codes
- [ ] **Business Logic**: Test conversation history, user progress tracking
- [ ] **Utility Functions**: Test audio file handling, data transformations
- [ ] **Configuration**: Test model selection logic, environment setup

**Frontend Unit Tests**  
- [ ] **Components**: Test UI components without audio dependencies
- [ ] **Services**: Test API client error handling and data transformation
- [ ] **State Management**: Test conversation state, recording state
- [ ] **Utilities**: Test audio formatting, validation helpers

### AI Component Testing

**Ollama/LLM Testing**
- [ ] **Integration tests**: Verify model loading and basic response generation
- [ ] **Response validation**: Test for appropriate German language output
- [ ] **Error handling**: Test offline scenarios, model unavailable
- [ ] **Performance tests**: Measure response times under load

**Speech Processing Testing**
- [ ] **Whisper STT**: Test with known German audio samples
- [ ] **TTS Quality**: Generate test audio and verify output quality
- [ ] **Audio Format Handling**: Test various input formats (WAV, MP3, etc.)
- [ ] **Pipeline Integration**: Test STT → LLM → TTS complete flow

### Integration Testing

**End-to-End Voice Conversation**
- [ ] Record sample German audio files for consistent testing
- [ ] Test complete voice interaction pipeline
- [ ] Validate conversation state persistence
- [ ] Test adaptive difficulty adjustments

**API Integration Testing**
- [ ] Test frontend → backend communication
- [ ] Test file upload/download flows
- [ ] Test real-time audio streaming (if implemented)
- [ ] Test error propagation from backend to frontend

### Performance Testing

**Response Time Benchmarks**
- [ ] Measure STT processing times for various audio lengths
- [ ] Track LLM response generation across conversation lengths
- [ ] Monitor TTS generation performance
- [ ] Profile memory usage during extended conversations

**Load Testing**
- [ ] Test multiple concurrent conversations (if supporting)
- [ ] Measure resource usage under sustained load
- [ ] Test model performance degradation over time

### Error Scenario Testing

**AI Service Failures**
- [ ] **Ollama offline**: Test graceful degradation or error messages
- [ ] **Model loading failures**: Test fallback to smaller models
- [ ] **Audio processing errors**: Test malformed audio file handling
- [ ] **Network issues**: Test offline mode functionality

**Edge Cases**
- [ ] **Very long conversations**: Test memory management
- [ ] **Rapid user inputs**: Test queuing and processing
- [ ] **Mixed languages**: Test German-only enforcement
- [ ] **Silent audio**: Test empty/silent audio file handling

### Manual Testing Procedures

**AI Quality Assessment**
- [ ] **German accuracy**: Regular manual evaluation of LLM German quality
- [ ] **Pronunciation**: Listen to TTS output for naturalness
- [ ] **Conversation flow**: Test natural conversation progression
- [ ] **Difficulty adaptation**: Verify appropriate level adjustments

**User Experience Testing**
- [ ] **Audio recording quality**: Test microphone input across devices
- [ ] **Response timing**: Evaluate perceived responsiveness
- [ ] **Error recovery**: Test user experience during failures
- [ ] **Accessibility**: Test keyboard navigation, screen reader compatibility

### Testing in Development Workflow

**Daily Testing Checklist**
1. **Quick smoke tests**: Run core functionality tests before committing
2. **Component tests**: Test specific features being developed
3. **Integration check**: Verify end-to-end pipeline still works
4. **Performance check**: Monitor response times haven't degraded

**Pre-commit Testing**
- [ ] Run all unit tests: `pytest backend/tests/`
- [ ] Run frontend tests: `npm run test`
- [ ] Type checking: `mypy backend/` and `npm run type-check`
- [ ] Basic integration test: Record → process → playback workflow

**Testing Commands**
```bash
# Backend testing
cd backend
pytest -v                          # Run all tests
pytest tests/test_ai_services.py   # Run specific test file
pytest -k "audio"                  # Run tests matching pattern

# Frontend testing  
cd frontend
npm run test                       # Run all tests
npm run test:coverage             # Run with coverage report
npm run test -- --watch          # Watch mode for development
```

### Test Data Management

**Audio Test Samples**
- [ ] Create collection of German audio samples at different proficiency levels
- [ ] Include edge cases: accented speech, background noise, quiet speech
- [ ] Store in `tests/fixtures/audio/` with consistent naming

**Conversation Test Data**
- [ ] Prepare conversation scenarios for different difficulty levels
- [ ] Create mock user progress states for testing adaptation
- [ ] Include problematic phrases that might break the AI pipeline

**Performance Baselines**
- [ ] Record initial performance benchmarks after each phase
- [ ] Track performance regression across development
- [ ] Document acceptable performance ranges for each component

---

## Current Status

**Overall Progress:** 0% Complete  
**Current Phase:** Phase 1 - AI Foundation Setup  
**Next Milestone:** Working FastAPI endpoint with German LLM  
**Blockers:** None currently  

**Last Updated:** [Update date when you modify this file]

---

## Architectural Implementation Details

### Error Handling & Monitoring Strategy

**Ollama Service Management**
- [ ] Implement health check endpoint: `/health/ollama`
- [ ] Auto-restart logic: Detect Ollama crashes, attempt restart (max 3 times)
- [ ] Model fallback hierarchy: OpenEuroLLM-German (7B) → SmolLM2-German (360M) → Error state
- [ ] Service status monitoring: Track model loading, memory usage, response times

**Audio Processing Failure Handling**
- [ ] STT failures: Retry once, then offer text input mode
- [ ] TTS failures: Show text response with retry audio button
- [ ] Audio recording failures: Clear error messages, permissions check
- [ ] File format errors: Convert unsupported formats or reject with helpful message

**User Experience During Errors**
- [ ] Loading indicators: Show "Processing speech...", "Generating response...", "Converting to speech..."
- [ ] Error notifications: Toast notifications for transient errors
- [ ] Graceful degradation: Always offer text mode as backup
- [ ] Recovery mechanisms: Clear "retry" buttons, session reset options

### Data Management Implementation

**Database Setup (SQLite)**
```sql
-- Conversation storage schema
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_input TEXT NOT NULL,
    user_audio_path TEXT,
    ai_response TEXT NOT NULL,
    ai_audio_path TEXT,
    difficulty_level TEXT,
    processing_time_ms INTEGER
);

-- User progress tracking
CREATE TABLE user_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vocabulary_encountered TEXT, -- JSON array
    grammar_topics TEXT,         -- JSON array  
    difficulty_level TEXT,
    session_count INTEGER DEFAULT 0,
    total_conversations INTEGER DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Data Persistence Strategy**
- [ ] Database location: `~/.german-tutor/conversations.db`
- [ ] Audio file storage: `~/.german-tutor/audio/` with UUID filenames
- [ ] Conversation export: JSON format for backup/sharing
- [ ] Data cleanup: User-configurable retention (default: 30 days)
- [ ] Privacy controls: Complete data wipe option, no cloud sync

**Model and Cache Management** 
- [ ] Model download location: `~/.german-tutor/models/`
- [ ] Cache policies: Audio files deleted after 24 hours, conversation audio retained per user settings
- [ ] Disk space monitoring: Alert if >2GB used, cleanup suggestions
- [ ] Model verification: Check model integrity on startup

### Configuration Management

**Environment Configuration**
```bash
# .env file template
DATABASE_PATH=~/.german-tutor/conversations.db
AUDIO_STORAGE_PATH=~/.german-tutor/audio/
MODEL_STORAGE_PATH=~/.german-tutor/models/

# Model configuration
PRIMARY_MODEL=openeurollm-german:7b
FALLBACK_MODEL=smollm2-german:360m
MAX_CONVERSATION_LENGTH=100

# Audio settings
AUDIO_FORMAT=wav
SAMPLE_RATE=16000
RECORDING_TIMEOUT_SECONDS=30

# API settings  
BACKEND_HOST=localhost
BACKEND_PORT=8000
FRONTEND_PORT=5173

# Performance settings
MAX_MEMORY_USAGE_GB=12
ENABLE_GPU_ACCELERATION=true
```

**Hardware Detection & Model Selection**
- [ ] RAM detection: Automatically select model based on available memory
- [ ] GPU detection: Enable GPU acceleration if available (Metal on M2)
- [ ] CPU cores: Adjust parallel processing based on core count
- [ ] Storage check: Verify sufficient disk space before model downloads

**Runtime Configuration**
- [ ] Settings UI: Allow users to change models, audio devices, storage locations
- [ ] Validation: Check configuration validity on startup
- [ ] Migration: Handle configuration file updates across versions
- [ ] Defaults: Sensible defaults for different hardware configurations

### Security Implementation

**Audio File Validation**
```python
# File validation rules
ALLOWED_AUDIO_FORMATS = ['wav', 'mp3', 'flac', 'm4a']
MAX_FILE_SIZE_MB = 50
MAX_DURATION_MINUTES = 5

# Validation implementation
def validate_audio_file(file_path: str) -> bool:
    # Check file size, format, duration
    # Scan for malicious content
    # Validate audio headers
    pass
```

**AI Output Sanitization**
- [ ] Content filtering: Remove potentially harmful content from AI responses
- [ ] Language validation: Ensure responses are primarily in German
- [ ] Response length limits: Prevent extremely long responses
- [ ] Profanity filtering: Block inappropriate content

**Secure File Handling**
- [ ] Temp file management: Secure creation/deletion of temporary audio files
- [ ] Input sanitization: Validate all user inputs, file names, paths
- [ ] Path traversal prevention: Restrict file access to designated directories
- [ ] Permissions: Minimal file permissions, non-executable audio files

**User Data Protection**
- [ ] Local encryption: Encrypt conversation database at rest (optional)
- [ ] Secure deletion: Overwrite deleted files, clear memory after use
- [ ] Data isolation: Separate user data from application code
- [ ] Privacy by design: No telemetry, no data transmission

### Documentation Standards

**API Documentation (Auto-generated)**
```python
# FastAPI automatic documentation
@app.post("/conversation", response_model=ConversationResponse)
async def process_conversation(
    request: ConversationRequest
) -> ConversationResponse:
    """
    Process a German conversation turn with voice input/output.
    
    Args:
        request: Contains audio data, conversation context, user level
        
    Returns:
        AI response with German text and audio
        
    Raises:
        HTTPException: If audio processing fails or AI model unavailable
    """
    pass
```

**Code Documentation Requirements**
- [ ] Function docstrings: All public functions must have docstrings
- [ ] Type annotations: All functions must have complete type hints
- [ ] Inline comments: Complex logic must have explanatory comments
- [ ] Module documentation: Each module needs purpose and usage examples

**User Documentation Structure**
```
docs/
├── README.md              # Quick start guide
├── installation.md        # Detailed setup instructions
├── troubleshooting.md     # Common issues and solutions
├── configuration.md       # Configuration options
├── api.md                # API reference (generated)
└── development.md        # Contributing guidelines
```

**Documentation Content Standards**
- [ ] Installation guide: Step-by-step with screenshots for major platforms
- [ ] Troubleshooting: Common errors with specific solutions
- [ ] Configuration guide: All settings explained with examples
- [ ] API reference: Auto-generated from code with examples
- [ ] Development setup: How to contribute to the project

---