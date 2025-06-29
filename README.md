# Adaptive Prompt Optimizer

A powerful web-based tool that optimizes prompts for specific AI coding tools, helping developers get better results from their AI assistants.

## 🚀 Features

- **Multi-Tool Support**: Optimizes prompts for 6+ popular AI coding tools:
  - GitHub Copilot
  - Cursor AI
  - Replit AI
  - Amazon CodeWhisperer
  - Tabnine
  - Codium AI

- **Intelligent Analysis**: Analyzes prompt intent, complexity, programming language, and keywords
- **Tool-Specific Optimization**: Applies unique optimization strategies based on each tool's strengths
- **Before/After Comparison**: Clear visual comparison of original vs optimized prompts
- **Detailed Explanations**: Explains what optimizations were made and why
- **Modern Web Interface**: Beautiful, responsive design with intuitive user experience

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd w3d3a3
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## 📖 How to Use

1. **Enter Your Prompt**: Type or paste your base prompt in the text area
2. **Select Target Tool**: Choose which AI coding tool you want to optimize for
3. **Click Optimize**: The system will analyze and optimize your prompt
4. **Review Results**: Compare the original and optimized prompts, along with detailed explanations

## 🎯 Optimization Strategies

### GitHub Copilot
- Adds specific type hints and function signatures
- Includes clear variable names and context
- Breaks complex requests into focused tasks
- Uses descriptive comments to guide generation

### Cursor AI
- Specifies exact locations for code changes
- Provides clear before/after examples
- Uses precise action verbs (refactor, optimize, fix)
- Includes relevant file context and imports

### Replit AI
- Breaks down complex tasks into learning steps
- Requests complete, runnable examples
- Asks for explanations alongside code
- Specifies target skill level

### Amazon CodeWhisperer
- Mentions relevant AWS services and integrations
- Includes security and compliance requirements
- Requests scalable and maintainable solutions
- Specifies deployment and infrastructure context

### Tabnine
- References existing code patterns in projects
- Mentions team coding standards and conventions
- Requests consistency with existing codebase style
- Includes relevant file and class context

### Codium AI
- Requests comprehensive test coverage
- Specifies edge cases and error scenarios
- Asks for code quality improvements
- Includes performance and maintainability considerations

## 🏗️ Architecture

```
w3d3a3/
├── app.py                 # Flask backend with optimization logic
├── templates/
│   └── index.html        # Frontend web interface
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

### Backend (Flask)
- **PromptOptimizer Class**: Core optimization engine
- **Analysis Engine**: Detects intent, complexity, and language
- **Tool-Specific Strategies**: Customized optimization for each AI tool
- **REST API**: Endpoints for optimization and tool information

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design**: Works on desktop and mobile devices
- **Interactive Tool Selection**: Visual cards for each AI tool
- **Real-time Results**: Instant display of optimization results
- **Modern UI**: Clean, professional interface with smooth animations

## 🔧 API Endpoints

### `POST /api/optimize`
Optimizes a prompt for a specific tool.

**Request Body**:
```json
{
  "prompt": "Your base prompt here",
  "tool": "copilot"
}
```

**Response**:
```json
{
  "original_prompt": "...",
  "optimized_prompt": "...",
  "analysis": {
    "intent": "creation",
    "complexity": "moderate",
    "language": "python",
    "keywords": [...],
    "length": 25
  },
  "explanations": [...],
  "tool": "GitHub Copilot"
}
```

### `GET /api/tools`
Returns information about all supported AI tools.

## 🎨 Customization

### Adding New AI Tools

1. Add tool configuration to the `tools` dictionary in `app.py`:
```python
'new_tool': {
    'name': 'New AI Tool',
    'strengths': ['strength1', 'strength2'],
    'preferences': ['preference1', 'preference2'],
    'optimization_strategies': ['strategy1', 'strategy2']
}
```

2. Add optimization logic in the `_apply_optimizations` method
3. The frontend will automatically display the new tool

### Modifying Optimization Strategies

Edit the `_apply_optimizations` method in the `PromptOptimizer` class to customize how prompts are optimized for each tool.

## 🚀 Demo

### Example Input:
```
Create a function that validates email addresses
```

### Optimized for GitHub Copilot:
```
In python, Create a function that validates email addresses

Please include type hints and clear parameter names.
```

### Optimized for Replit AI:
```
Break this down step by step: Create a function that validates email addresses

Please provide a complete, runnable example with explanations.

Make sure the code is beginner-friendly and well-commented.
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with Flask and modern web technologies
- Inspired by the need for better AI tool interaction
- Designed for developers who want to maximize their AI coding assistant effectiveness