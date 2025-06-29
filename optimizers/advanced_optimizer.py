import re
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class OptimizationRule:
    """Represents a single optimization rule."""
    pattern: str
    replacement: str
    condition: Optional[str] = None
    priority: int = 1

class AdvancedPromptOptimizer:
    """Advanced prompt optimizer with pattern-based rules and context awareness."""
    
    def __init__(self):
        self.optimization_rules = self._load_optimization_rules()
        self.context_patterns = self._load_context_patterns()
        
    def _load_optimization_rules(self) -> Dict[str, List[OptimizationRule]]:
        """Load optimization rules for each tool."""
        return {
            'copilot': [
                OptimizationRule(
                    pattern=r'create a function',
                    replacement='create a well-documented function with type hints',
                    condition='python'
                ),
                OptimizationRule(
                    pattern=r'write code',
                    replacement='write clean, readable code with appropriate comments',
                    priority=2
                ),
                OptimizationRule(
                    pattern=r'implement (.+)',
                    replacement=r'implement \1 with proper error handling and edge case consideration',
                    priority=1
                )
            ],
            'cursor': [
                OptimizationRule(
                    pattern=r'fix (.+)',
                    replacement=r'identify and fix \1 in the specified file location',
                    priority=1
                ),
                OptimizationRule(
                    pattern=r'refactor',
                    replacement='refactor the code while maintaining existing functionality',
                    priority=2
                )
            ],
            'replit': [
                OptimizationRule(
                    pattern=r'create (.+)',
                    replacement=r'create \1 with step-by-step explanations for learning',
                    priority=1
                ),
                OptimizationRule(
                    pattern=r'build (.+)',
                    replacement=r'build \1 as a complete, runnable example with educational comments',
                    priority=1
                )
            ]
        }
    
    def _load_context_patterns(self) -> Dict[str, List[str]]:
        """Load context enhancement patterns."""
        return {
            'security': [
                'include input validation',
                'implement proper error handling',
                'consider security best practices',
                'add authentication if needed'
            ],
            'performance': [
                'optimize for performance',
                'consider memory usage',
                'implement efficient algorithms',
                'add caching where appropriate'
            ],
            'testing': [
                'include unit tests',
                'cover edge cases',
                'add integration tests',
                'implement test fixtures'
            ],
            'documentation': [
                'add comprehensive docstrings',
                'include usage examples',
                'document parameters and return values',
                'add inline comments for complex logic'
            ]
        }
    
    def optimize_prompt(self, prompt: str, tool: str, context: Dict = None) -> Tuple[str, List[str]]:
        """Optimize a prompt using advanced pattern matching and context awareness."""
        optimized_prompt = prompt
        applied_optimizations = []
        
        # Apply tool-specific rules
        if tool in self.optimization_rules:
            optimized_prompt, tool_optimizations = self._apply_tool_rules(
                optimized_prompt, self.optimization_rules[tool]
            )
            applied_optimizations.extend(tool_optimizations)
        
        # Apply context-based enhancements
        if context:
            optimized_prompt, context_optimizations = self._apply_context_enhancements(
                optimized_prompt, context
            )
            applied_optimizations.extend(context_optimizations)
        
        # Apply general improvements
        optimized_prompt, general_optimizations = self._apply_general_improvements(
            optimized_prompt, tool
        )
        applied_optimizations.extend(general_optimizations)
        
        return optimized_prompt, applied_optimizations
    
    def _apply_tool_rules(self, prompt: str, rules: List[OptimizationRule]) -> Tuple[str, List[str]]:
        """Apply tool-specific optimization rules."""
        optimized = prompt
        applied = []
        
        # Sort rules by priority
        sorted_rules = sorted(rules, key=lambda r: r.priority)
        
        for rule in sorted_rules:
            if rule.condition and rule.condition.lower() not in prompt.lower():
                continue
                
            if re.search(rule.pattern, optimized, re.IGNORECASE):
                optimized = re.sub(rule.pattern, rule.replacement, optimized, flags=re.IGNORECASE)
                applied.append(f"Applied rule: {rule.pattern} -> {rule.replacement}")
        
        return optimized, applied
    
    def _apply_context_enhancements(self, prompt: str, context: Dict) -> Tuple[str, List[str]]:
        """Apply context-based enhancements."""
        optimized = prompt
        applied = []
        
        for context_type, requirements in context.items():
            if context_type in self.context_patterns:
                enhancements = self.context_patterns[context_type]
                if requirements:  # If context is requested
                    selected_enhancements = enhancements[:2]  # Limit to avoid overwhelming
                    enhancement_text = '. '.join(selected_enhancements)
                    optimized += f"\n\nAdditional requirements: {enhancement_text}."
                    applied.append(f"Added {context_type} context enhancements")
        
        return optimized, applied
    
    def _apply_general_improvements(self, prompt: str, tool: str) -> Tuple[str, List[str]]:
        """Apply general improvements based on best practices."""
        optimized = prompt
        applied = []
        
        # Add specificity if prompt is too vague
        if len(prompt.split()) < 10:
            optimized += "\n\nPlease provide a complete, detailed implementation."
            applied.append("Added specificity to short prompt")
        
        # Add language context if not specified
        languages = ['python', 'javascript', 'java', 'c++', 'c#', 'go', 'rust']
        if not any(lang in prompt.lower() for lang in languages):
            optimized = f"Using an appropriate programming language, {optimized}"
            applied.append("Added programming language context")
        
        # Tool-specific general improvements
        if tool == 'copilot':
            if 'function' in prompt.lower() and 'type' not in prompt.lower():
                optimized += "\n\nInclude appropriate type annotations."
                applied.append("Added type annotation requirement for Copilot")
        
        elif tool == 'replit':
            if 'explain' not in prompt.lower():
                optimized += "\n\nInclude explanations to help with learning."
                applied.append("Added educational context for Replit")
        
        elif tool == 'codewhisperer':
            if 'security' not in prompt.lower():
                optimized += "\n\nConsider security best practices."
                applied.append("Added security consideration for CodeWhisperer")
        
        return optimized, applied
    
    def analyze_prompt_quality(self, prompt: str) -> Dict[str, float]:
        """Analyze the quality of a prompt and return metrics."""
        metrics = {
            'specificity': self._calculate_specificity(prompt),
            'clarity': self._calculate_clarity(prompt),
            'completeness': self._calculate_completeness(prompt),
            'technical_depth': self._calculate_technical_depth(prompt)
        }
        return metrics
    
    def _calculate_specificity(self, prompt: str) -> float:
        """Calculate how specific the prompt is (0-1 scale)."""
        specific_words = ['function', 'class', 'method', 'variable', 'parameter', 'return', 'input', 'output']
        word_count = len(prompt.split())
        specific_count = sum(1 for word in specific_words if word in prompt.lower())
        
        if word_count == 0:
            return 0.0
        
        return min(specific_count / (word_count * 0.1), 1.0)
    
    def _calculate_clarity(self, prompt: str) -> float:
        """Calculate how clear the prompt is (0-1 scale)."""
        # Simple heuristic: longer sentences and complex words reduce clarity
        sentences = prompt.split('.')
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        
        # Optimal sentence length is around 15-20 words
        clarity_score = 1.0 - abs(avg_sentence_length - 17.5) / 17.5
        return max(0.0, min(clarity_score, 1.0))
    
    def _calculate_completeness(self, prompt: str) -> float:
        """Calculate how complete the prompt is (0-1 scale)."""
        completeness_indicators = [
            'input', 'output', 'example', 'requirement', 'constraint',
            'error', 'handle', 'test', 'validate'
        ]
        
        present_indicators = sum(1 for indicator in completeness_indicators 
                               if indicator in prompt.lower())
        
        return min(present_indicators / len(completeness_indicators), 1.0)
    
    def _calculate_technical_depth(self, prompt: str) -> float:
        """Calculate the technical depth of the prompt (0-1 scale)."""
        technical_terms = [
            'algorithm', 'data structure', 'complexity', 'performance',
            'optimization', 'pattern', 'architecture', 'framework',
            'library', 'api', 'database', 'async', 'concurrent'
        ]
        
        present_terms = sum(1 for term in technical_terms if term in prompt.lower())
        return min(present_terms / 5, 1.0)  # Normalize to 5 terms for full score
    
    def suggest_improvements(self, prompt: str, quality_metrics: Dict[str, float]) -> List[str]:
        """Suggest improvements based on quality metrics."""
        suggestions = []
        
        if quality_metrics['specificity'] < 0.5:
            suggestions.append("Add more specific technical terms and requirements")
        
        if quality_metrics['clarity'] < 0.5:
            suggestions.append("Break down complex sentences into simpler ones")
        
        if quality_metrics['completeness'] < 0.5:
            suggestions.append("Include input/output examples and error handling requirements")
        
        if quality_metrics['technical_depth'] < 0.3:
            suggestions.append("Add more technical context and implementation details")
        
        return suggestions

# Example usage and testing
if __name__ == "__main__":
    optimizer = AdvancedPromptOptimizer()
    
    # Test prompt
    test_prompt = "create a function that validates emails"
    
    # Test optimization
    optimized, explanations = optimizer.optimize_prompt(
        test_prompt, 
        'copilot', 
        {'security': True, 'testing': True}
    )
    
    print(f"Original: {test_prompt}")
    print(f"Optimized: {optimized}")
    print(f"Explanations: {explanations}")
    
    # Test quality analysis
    quality = optimizer.analyze_prompt_quality(test_prompt)
    print(f"Quality metrics: {quality}")
    
    suggestions = optimizer.suggest_improvements(test_prompt, quality)
    print(f"Suggestions: {suggestions}")