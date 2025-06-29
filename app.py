from flask import Flask, render_template, request, jsonify
import json
import re
from typing import Dict, List, Tuple

app = Flask(__name__)

class PromptOptimizer:
    def __init__(self):
        self.tools = {
            'copilot': {
                'name': 'GitHub Copilot',
                'strengths': ['code completion', 'context awareness', 'multi-language support'],
                'preferences': ['clear function signatures', 'descriptive variable names', 'inline comments'],
                'optimization_strategies': [
                    'Add specific type hints and function signatures',
                    'Include clear variable names and context',
                    'Break complex requests into smaller, focused tasks',
                    'Use descriptive comments to guide code generation'
                ]
            },
            'cursor': {
                'name': 'Cursor AI',
                'strengths': ['code editing', 'refactoring', 'debugging'],
                'preferences': ['specific edit instructions', 'clear before/after examples', 'focused scope'],
                'optimization_strategies': [
                    'Specify exact locations for code changes',
                    'Provide clear before/after examples',
                    'Use precise action verbs (refactor, optimize, fix)',
                    'Include relevant file context and imports'
                ]
            },
            'replit': {
                'name': 'Replit AI',
                'strengths': ['rapid prototyping', 'educational code', 'web development'],
                'preferences': ['step-by-step instructions', 'beginner-friendly explanations', 'complete examples'],
                'optimization_strategies': [
                    'Break down complex tasks into learning steps',
                    'Request complete, runnable examples',
                    'Ask for explanations alongside code',
                    'Specify the target skill level (beginner/intermediate/advanced)'
                ]
            },
            'codewhisperer': {
                'name': 'Amazon CodeWhisperer',
                'strengths': ['AWS integration', 'security best practices', 'enterprise patterns'],
                'preferences': ['AWS service context', 'security considerations', 'scalable patterns'],
                'optimization_strategies': [
                    'Mention relevant AWS services and integrations',
                    'Include security and compliance requirements',
                    'Request scalable and maintainable solutions',
                    'Specify deployment and infrastructure context'
                ]
            },
            'tabnine': {
                'name': 'Tabnine',
                'strengths': ['local context', 'team patterns', 'code consistency'],
                'preferences': ['consistent coding style', 'team conventions', 'local codebase patterns'],
                'optimization_strategies': [
                    'Reference existing code patterns in your project',
                    'Mention team coding standards and conventions',
                    'Request consistency with existing codebase style',
                    'Include relevant file and class context'
                ]
            },
            'codium': {
                'name': 'Codium AI',
                'strengths': ['test generation', 'code analysis', 'quality assurance'],
                'preferences': ['test scenarios', 'edge cases', 'code quality metrics'],
                'optimization_strategies': [
                    'Request comprehensive test coverage',
                    'Specify edge cases and error scenarios',
                    'Ask for code quality improvements',
                    'Include performance and maintainability considerations'
                ]
            }
        }
    
    def analyze_prompt(self, prompt: str) -> Dict:
        """Analyze the input prompt to understand intent and complexity."""
        analysis = {
            'intent': self._detect_intent(prompt),
            'complexity': self._assess_complexity(prompt),
            'language': self._detect_language(prompt),
            'keywords': self._extract_keywords(prompt),
            'length': len(prompt.split())
        }
        return analysis
    
    def _detect_intent(self, prompt: str) -> str:
        """Detect the primary intent of the prompt."""
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['create', 'build', 'implement', 'develop']):
            return 'creation'
        elif any(word in prompt_lower for word in ['fix', 'debug', 'error', 'bug']):
            return 'debugging'
        elif any(word in prompt_lower for word in ['refactor', 'improve', 'optimize', 'clean']):
            return 'refactoring'
        elif any(word in prompt_lower for word in ['test', 'unit test', 'testing']):
            return 'testing'
        elif any(word in prompt_lower for word in ['explain', 'understand', 'how', 'what']):
            return 'explanation'
        else:
            return 'general'
    
    def _assess_complexity(self, prompt: str) -> str:
        """Assess the complexity level of the prompt."""
        word_count = len(prompt.split())
        technical_terms = len(re.findall(r'\b(?:class|function|method|algorithm|database|API|framework|library)\b', prompt.lower()))
        
        if word_count < 10 and technical_terms < 2:
            return 'simple'
        elif word_count < 30 and technical_terms < 5:
            return 'moderate'
        else:
            return 'complex'
    
    def _detect_language(self, prompt: str) -> str:
        """Detect programming language mentioned in the prompt."""
        languages = ['python', 'javascript', 'java', 'c++', 'c#', 'go', 'rust', 'typescript', 'php', 'ruby']
        prompt_lower = prompt.lower()
        
        for lang in languages:
            if lang in prompt_lower:
                return lang
        return 'general'
    
    def _extract_keywords(self, prompt: str) -> List[str]:
        """Extract important keywords from the prompt."""
        # Simple keyword extraction - in a real implementation, you might use NLP libraries
        words = re.findall(r'\b\w+\b', prompt.lower())
        technical_keywords = [word for word in words if len(word) > 3 and 
                            word in ['function', 'class', 'method', 'variable', 'algorithm', 'database', 
                                   'api', 'framework', 'library', 'server', 'client', 'frontend', 'backend']]
        return list(set(technical_keywords))
    
    def optimize_for_tool(self, prompt: str, tool_id: str) -> Tuple[str, List[str]]:
        """Optimize the prompt for a specific tool."""
        if tool_id not in self.tools:
            return prompt, ["Tool not found"]
        
        tool = self.tools[tool_id]
        analysis = self.analyze_prompt(prompt)
        
        optimized_prompt = self._apply_optimizations(prompt, tool, analysis)
        explanations = self._generate_explanations(prompt, optimized_prompt, tool, analysis)
        
        return optimized_prompt, explanations
    
    def _apply_optimizations(self, prompt: str, tool: Dict, analysis: Dict) -> str:
        """Apply tool-specific optimizations to the prompt."""
        optimized = prompt
        
        # Add context based on tool strengths
        if tool['name'] == 'GitHub Copilot':
            if analysis['intent'] == 'creation' and analysis['language'] != 'general':
                optimized = f"In {analysis['language']}, {optimized}"
            if 'function' in analysis['keywords']:
                optimized += "\n\nPlease include type hints and clear parameter names."
        
        elif tool['name'] == 'Cursor AI':
            if analysis['intent'] == 'refactoring':
                optimized = f"Please refactor the following code: {optimized}\n\nProvide the complete updated code with clear explanations of changes made."
            elif analysis['intent'] == 'debugging':
                optimized = f"Debug this code issue: {optimized}\n\nPlease identify the problem and provide the corrected code."
        
        elif tool['name'] == 'Replit AI':
            if analysis['complexity'] == 'complex':
                optimized = f"Break this down step by step: {optimized}\n\nPlease provide a complete, runnable example with explanations."
            optimized += "\n\nMake sure the code is beginner-friendly and well-commented."
        
        elif tool['name'] == 'Amazon CodeWhisperer':
            if 'api' in analysis['keywords'] or 'server' in analysis['keywords']:
                optimized += "\n\nPlease consider AWS best practices and security implications."
            if analysis['intent'] == 'creation':
                optimized += "\n\nInclude error handling and scalability considerations."
        
        elif tool['name'] == 'Tabnine':
            optimized = f"Following our team's coding standards: {optimized}\n\nPlease maintain consistency with existing codebase patterns."
        
        elif tool['name'] == 'Codium AI':
            if analysis['intent'] != 'testing':
                optimized += "\n\nAlso generate comprehensive unit tests for this code."
            optimized += "\n\nInclude edge cases and error scenarios in the tests."
        
        return optimized
    
    def _generate_explanations(self, original: str, optimized: str, tool: Dict, analysis: Dict) -> List[str]:
        """Generate explanations for the optimizations made."""
        explanations = []
        
        if len(optimized) > len(original):
            explanations.append(f"Added context and specifications optimized for {tool['name']}'s strengths")
        
        if analysis['language'] != 'general':
            explanations.append(f"Specified programming language ({analysis['language']}) for better context")
        
        if analysis['intent'] == 'creation':
            explanations.append("Enhanced prompt for code creation with specific requirements")
        elif analysis['intent'] == 'debugging':
            explanations.append("Structured prompt for effective debugging assistance")
        elif analysis['intent'] == 'refactoring':
            explanations.append("Optimized for code improvement and refactoring guidance")
        
        explanations.extend([f"Leveraged {tool['name']}'s strength in {strength}" for strength in tool['strengths'][:2]])
        
        return explanations

optimizer = PromptOptimizer()

@app.route('/')
def index():
    return render_template('index.html', tools=optimizer.tools)

@app.route('/api/optimize', methods=['POST'])
def optimize_prompt():
    data = request.json
    prompt = data.get('prompt', '')
    tool_id = data.get('tool', '')
    
    if not prompt or not tool_id:
        return jsonify({'error': 'Missing prompt or tool selection'}), 400
    
    analysis = optimizer.analyze_prompt(prompt)
    optimized_prompt, explanations = optimizer.optimize_for_tool(prompt, tool_id)
    
    return jsonify({
        'original_prompt': prompt,
        'optimized_prompt': optimized_prompt,
        'analysis': analysis,
        'explanations': explanations,
        'tool': optimizer.tools[tool_id]['name']
    })

@app.route('/api/tools')
def get_tools():
    return jsonify(optimizer.tools)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)