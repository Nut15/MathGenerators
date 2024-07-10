import additionGenerator
import subtractionGenerator

additionGenerator.additionGenerator(page_break=False, start=True)
subtractionGenerator.subtractionGenerator(page_break=True, start=True, length=2)
subtractionGenerator.subtractionGenerator(page_break=False, start=False)