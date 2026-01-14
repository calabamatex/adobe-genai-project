"""Abstract base class for image generation services."""
from abc import ABC, abstractmethod
from typing import Optional
from src.models import ComprehensiveBrandGuidelines


class ImageGenerationService(ABC):
    """Abstract base class for all image generation backends."""
    
    def __init__(self, api_key: str, max_retries: int = 3):
        self.api_key = api_key
        self.max_retries = max_retries
        self.backend_name = self.__class__.__name__
    
    @abstractmethod
    async def generate_image(
        self,
        prompt: str,
        size: str = "1024x1024",
        brand_guidelines: Optional[ComprehensiveBrandGuidelines] = None
    ) -> bytes:
        """
        Generate an image from text prompt.
        
        Args:
            prompt: Text description of the image to generate
            size: Image dimensions (format depends on backend)
            brand_guidelines: Optional brand guidelines to apply
            
        Returns:
            bytes: Raw image data
        """
        pass
    
    def _build_brand_compliant_prompt(
        self,
        base_prompt: str,
        guidelines: Optional[ComprehensiveBrandGuidelines]
    ) -> str:
        """
        Enhance prompt with brand guidelines.
        
        This is a shared utility method that all backends can use.
        """
        if not guidelines:
            return base_prompt
        
        enhanced = base_prompt
        
        if guidelines.photography_style:
            enhanced += f", {guidelines.photography_style}"
        
        if guidelines.brand_voice:
            enhanced += f", {guidelines.brand_voice} aesthetic"
        
        # Add prohibitions as negative prompts
        if guidelines.prohibited_elements:
            enhanced += f". Avoid: {', '.join(guidelines.prohibited_elements[:3])}"
        
        return enhanced
    
    @abstractmethod
    def get_backend_name(self) -> str:
        """Return the backend name for logging/reporting."""
        pass
    
    @abstractmethod
    def validate_config(self) -> tuple[bool, list[str]]:
        """Validate backend configuration."""
        pass
