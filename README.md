# Agentic AI Bootcamp Starter

A comprehensive starter repository for building **agentic AI systems** with multi-tool routing, memory, and persistence. This project demonstrates a complete agentic AI system that can use multiple tools, maintain conversation memory, and store long-term facts.

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/hariviapak/agentic-bootcamp-starter.git
cd agentic-bootcamp-starter

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 5. Run the application
python -m src.agentic_bootcamp.app
```

## ✨ Features

### 🤖 Multi-Tool Agent
- **Intelligent Tool Routing**: AI-powered selection of the right tool based on user input
- **Tool Validation**: Pydantic schemas ensure proper tool arguments
- **Fallback Handling**: Graceful fallback to LLM responses when no tool fits

### 🧠 Memory & Persistence
- **Short-term Memory**: Conversation buffer with automatic trimming
- **Long-term Memory**: Vector store for storing and retrieving facts
- **Fact Storage**: Dedicated tool for storing important information

### 🛠️ Available Tools
- **Math Calculator**: Evaluate mathematical expressions
- **Weather Lookup**: Get current weather for any city
- **File Reader**: Read and analyze text files
- **Unit Converter**: Convert between different units
- **Memory Tool**: Store and retrieve facts

## 🎯 Usage Examples

Once running, try these commands:

```
You: remember my GST number is 12345
You: what's my GST number?
You: I live in Mohali. remember this.
You: what did I tell you about where I live?
You: weather in Delhi
You: calculate 12*(4+5)
You: convert 10 km to miles
You: read file ./README.md
```

## 📁 Project Structure

```
agentic-bootcamp-starter/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── pyproject.toml           # Project configuration
├── Makefile                 # Development commands
├── src/
│   └── agentic_bootcamp/
│       ├── app.py           # Main application entry point
│       ├── config.py        # Configuration and environment loading
│       ├── llm_client.py    # LLM client abstraction
│       ├── planning.py      # ReAct loop and tool routing
│       ├── memory/
│       │   ├── conversation_memory.py  # Short-term conversation memory
│       │   └── vector_store.py         # Long-term vector storage
│       └── tools/
│           ├── __init__.py
│           ├── math_tool.py
│           ├── weather_tool.py
│           ├── file_reader_tool.py
│           ├── unit_converter.py
│           └── memory_tools.py
├── service/                 # FastAPI service (for future use)
└── tests/                   # Test suite
```

## 🔧 Configuration

The application uses environment variables for configuration. Copy `.env.example` to `.env` and set:

```bash
OPENAI_API_KEY=your_openai_api_key_here
MODEL_NAME=gpt-4o-mini
TEMPERATURE=0.3
```

## 🧪 Testing

```bash
# Run tests
pytest -q

# Or use the Makefile
make test
```

## 🛠️ Development

```bash
# Format code
make format

# Run the application
make run

# Set up development environment
make setup
```

## 🔄 How It Works

1. **Input Processing**: User input is received and added to conversation memory
2. **Tool Selection**: The AI analyzes the input and selects the most appropriate tool
3. **Tool Execution**: Selected tool is executed with validated arguments
4. **Memory Integration**: Relevant memory is retrieved and injected into the context
5. **Response Generation**: Final response is generated using tool results and memory
6. **Memory Storage**: New information is stored in both short-term and long-term memory

## 🚧 Roadmap

- **Week 1**: ✅ Basic LLM integration and tool calling
- **Week 2**: ✅ Multi-tool routing and ReAct loop
- **Week 3**: ✅ Memory and persistence (Current)
- **Week 4**: 🔄 FastAPI service and multi-agent orchestration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

This starter repository is designed for learning agentic AI concepts and building practical AI systems with modern tools and techniques.
