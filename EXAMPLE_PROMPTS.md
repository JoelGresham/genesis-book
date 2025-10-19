# The Genesis Code - ComfyUI Example Prompts

This document contains example prompts for generating artwork for "The Genesis Code" novel. Copy and paste these into the appropriate workflow's positive prompt field.

---

## INTERIOR BOOK DRAWINGS (Use with: comfyui_workflow_book_drawings.json)

These prompts create simple, clean sketch-style illustrations perfect for chapter headers, margins, and thought bubbles.

### DNA & Genetic Themes

```
sketch illustration, simple line art, DNA double helix diagram, clean scientific drawing, unfinished sketch style, minimal shading, pencil drawing, black and white, gene sequence visualization
```

```
sketch illustration, simple line art, chromosome structure, genetic code diagram, clean drawing, unfinished sketch style, minimal shading, thought bubble style, black and white
```

```
sketch illustration, simple line art, DNA strand unraveling, genetic activation markers, clean scientific diagram, unfinished sketch style, minimal shading, pencil drawing
```

### Dinosaur Sketches (Ancient/Scientific)

```
sketch illustration, simple line art, troodontid dinosaur head profile, intelligent expression, clean drawing, unfinished sketch style, minimal shading, scientific illustration, black and white
```

```
sketch illustration, simple line art, dinosaur arranging stones in pattern, overhead view, geometric shapes, clean drawing, unfinished sketch style, minimal shading, pencil drawing
```

```
sketch illustration, simple line art, dinosaur silhouette watching stars, night sky, constellation patterns, clean drawing, unfinished sketch style, minimal shading, black and white
```

```
sketch illustration, simple line art, ancient reptile studying small mammal, observational diagram, clean drawing, unfinished sketch style, minimal shading, scientific illustration
```

### Timeline & Mathematical Concepts

```
sketch illustration, simple line art, timeline visualization, connected points, mathematical progression, clean diagram, unfinished sketch style, minimal shading, black and white
```

```
sketch illustration, simple line art, fibonacci spiral, mathematical pattern, clean scientific drawing, unfinished sketch style, minimal shading, pencil drawing
```

```
sketch illustration, simple line art, technological milestone markers, progression chart, clean diagram, unfinished sketch style, minimal shading, black and white
```

```
sketch illustration, simple line art, asteroid trajectory calculation, orbital path diagram, clean scientific drawing, unfinished sketch style, minimal shading, pencil drawing
```

### Thought Bubbles & Concept Sketches

```
sketch illustration, simple line art, thought bubble containing DNA helix, consciousness visualization, clean drawing, unfinished sketch style, minimal shading, black and white
```

```
sketch illustration, simple line art, human brain connected to genetic code, neural pathways, clean scientific diagram, unfinished sketch style, minimal shading, pencil drawing
```

```
sketch illustration, simple line art, overlapping timelines ancient and modern, 65 million years, clean drawing, unfinished sketch style, minimal shading, black and white
```

```
sketch illustration, simple line art, compulsion visualization, neural activation pattern, clean scientific diagram, unfinished sketch style, minimal shading, pencil drawing
```

### Scientific Equipment & Lab Scenes

```
sketch illustration, simple line art, microscope viewing genetic sequence, laboratory equipment, clean drawing, unfinished sketch style, minimal shading, black and white
```

```
sketch illustration, simple line art, computer screen displaying DNA code, data visualization, clean diagram, unfinished sketch style, minimal shading, pencil drawing
```

```
sketch illustration, simple line art, satellite array in orbit, planetary defense grid, clean scientific drawing, unfinished sketch style, minimal shading, black and white
```

### Symbolic/Metaphorical

```
sketch illustration, simple line art, hands reaching across time, connection through ages, clean drawing, unfinished sketch style, minimal shading, black and white
```

```
sketch illustration, simple line art, stone pattern morphing into circuit board, ancient meets modern, clean drawing, unfinished sketch style, minimal shading, pencil drawing
```

```
sketch illustration, simple line art, chain of inheritance, species progression, clean scientific diagram, unfinished sketch style, minimal shading, black and white
```

---

## BOOK COVER DESIGNS (Use with: comfyui_workflow_book_cover.json)

These prompts create bold, enticing book covers that hint at the mystery without revealing the twist.

### Cover Concept 1: DNA Helix Dominant

```
book cover design, sci-fi novel, massive glowing DNA double helix rising from ancient landscape, mysterious atmosphere, dinosaur skeleton silhouette in foreground, dramatic lighting, bold composition, professional book cover, cinematic, stars and asteroid in sky, teal and amber color palette, high quality, epic scale
```

### Cover Concept 2: Ancient Meets Modern

```
book cover design, sci-fi novel, split composition ancient prehistoric world bottom modern cityscape top, DNA helix connecting both eras, mysterious atmosphere, dramatic lighting, bold composition, professional book cover, cinematic, deep blues and purples, high quality, symbolic imagery
```

### Cover Concept 3: The Watcher

```
book cover design, sci-fi novel, silhouette of intelligent dinosaur against starry sky, mathematical equations and genetic code overlaying the scene, mysterious atmosphere, dramatic lighting, bold composition, professional book cover, cinematic, dark blue and gold colors, high quality, contemplative mood
```

### Cover Concept 4: Genetic Timeline

```
book cover design, sci-fi novel, spiral timeline emanating from center, evolutionary stages and technological milestones, DNA strand as backbone, mysterious atmosphere, cosmic background, dramatic lighting, bold composition, professional book cover, cinematic, emerald and silver colors, high quality
```

### Cover Concept 5: Asteroid & Legacy

```
book cover design, sci-fi novel, approaching asteroid in space, Earth below, DNA double helix orbital path around planet, mysterious atmosphere, dramatic lighting, bold composition, professional book cover, cinematic, deep space blues and bright accents, high quality, sense of urgency
```

### Cover Concept 6: The Code Revealed

```
book cover design, sci-fi novel, close-up of genetic sequence with hidden mathematical patterns, glowing activation markers, mysterious atmosphere, matrix-like visualization, dramatic lighting, bold composition, professional book cover, cinematic, green and black with gold highlights, high quality, technical yet organic
```

### Cover Concept 7: Prehistoric Intelligence

```
book cover design, sci-fi novel, ancient stone patterns arranged in precise geometric formation, stars aligned above, DNA helix shadow cast on stones, mysterious atmosphere, twilight lighting, bold composition, professional book cover, cinematic, earth tones with cosmic purples, high quality, sense of ancient wisdom
```

### Cover Concept 8: Dual Perspective

```
book cover design, sci-fi novel, human scientist looking at genetic code on one side, dinosaur arranging stones on other side, mirror composition, mysterious atmosphere, dramatic lighting, bold composition, professional book cover, cinematic, contrasting warm and cool tones, high quality, parallel destinies
```

### Cover Concept 9: The Activation

```
book cover design, sci-fi novel, human figure with DNA helix illuminated inside transparent body, ancient dinosaur shadow behind, cosmic background, mysterious atmosphere, dramatic lighting, bold composition, professional book cover, cinematic, bioluminescent blues and purples, high quality, awakening theme
```

### Cover Concept 10: Simple & Iconic

```
book cover design, sci-fi novel, minimalist design, single DNA double helix vertical, half ancient stone texture half modern digital, black background, mysterious atmosphere, dramatic lighting, bold composition, professional book cover, cinematic, gold and silver gradient, high quality, elegant simplicity
```

---

## TIPS FOR BEST RESULTS

### For Interior Drawings:
- Keep prompts focused on "sketch illustration, simple line art"
- Always include "unfinished sketch style, minimal shading"
- Use "black and white" or "pencil drawing" for consistency
- Adjust LoRA strength (0.7-0.9) for more or less sketch effect
- Use CFG scale 6-8 for cleaner lines
- Generate multiple variations and pick the cleanest

### For Book Covers:
- Use descriptive mood words: "mysterious," "dramatic," "cinematic"
- Include color palette suggestions for consistency
- Try different CFG scales (7.5-9.5) for varying boldness
- Generate multiple seeds (change the seed number) to explore options
- The upscaler node will create high-res versions automatically
- Consider combining elements from multiple generations in post-processing

### Model Recommendations:

**For Interior Drawings, you'll need:**
- Base Model: `flux1-dev.safetensors` OR `sd_xl_base_1.0.safetensors`
- LoRA: Download "Sketch Illustration - Flux1-Dev" or "Pencil Sketch - ILLUSTRIOUS" from Civitai
  - Place in: `ComfyUI/models/loras/`

**For Book Covers, you'll need:**
- Base Model: `dreamshaperXL_v21TurboDPMSDE.safetensors` OR `deliberate_v3.safetensors`
- LoRA (Optional): "Book Cover - Flux" from Civitai
  - Place in: `ComfyUI/models/loras/`
- Upscale Model: `RealESRGAN_x4plus.pth`
  - Place in: `ComfyUI/models/upscale_models/`

### Where to Download Models:
- CivitAI: https://civitai.com
- HuggingFace: https://huggingface.co
- Search for model names mentioned above

---

## WORKFLOW CUSTOMIZATION

### Adjusting Image Size:
In the "EmptyLatentImage" node:
- Current: 768x1024 (portrait)
- For square: 1024x1024
- For landscape: 1024x768
- For cover: 768x1024 works well for standard book dimensions

### Adjusting Generation Quality:
In the "KSampler" node:
- Steps: 20-30 for sketches, 25-35 for covers
- CFG Scale: 6-8 for sketches, 7.5-9 for covers
- Sampler: "euler_ancestral" for sketches, "dpmpp_2m_sde" for covers
- Scheduler: "normal" for sketches, "karras" for covers

### Using Multiple LoRAs:
You can add additional LoRA loader nodes to combine styles:
1. Right-click → Add Node → LoraLoader
2. Connect the output of first LoRA to input of second
3. Adjust strength values (total shouldn't exceed 1.5-2.0 combined)

---

## BOOK-SPECIFIC SCENE PROMPTS

These are more detailed prompts for specific scenes from the outline:

### Chapter 1 - The Watcher's Introduction
```
sketch illustration, simple line art, dinosaur in clearing at dawn, watching sky, three stones in precise pattern, clean drawing, unfinished sketch style, minimal shading, peaceful atmosphere, black and white
```

### Chapter 7 - The Companion's Death
```
sketch illustration, simple line art, fallen dinosaur beside work site, stones scattered nearby, clean drawing, unfinished sketch style, minimal shading, somber mood, black and white, emotional weight
```

### Chapter 10 - The Reveal Moment
```
sketch illustration, simple line art, small mammal using stick tool, dinosaur observing, genetic code pattern faintly visible, clean scientific diagram, unfinished sketch style, minimal shading, black and white, moment of significance
```

### Chapter 22 - The Activation
```
sketch illustration, simple line art, human head profile with neural pathways lighting up, blueprint visions, clean drawing, unfinished sketch style, minimal shading, intense focus, black and white, compulsion visualization
```

### Chapter 29 - Connection Across Time
```
sketch illustration, simple line art, two silhouettes reaching toward each other, DNA helix between them, 65 million years apart, clean drawing, unfinished sketch style, minimal shading, black and white, emotional connection
```

---

## TESTING WORKFLOW

1. Load one of the workflow JSON files into ComfyUI
2. Replace the positive prompt with one from above
3. Click "Queue Prompt" to generate
4. If you get errors about missing models, download them from the sources above
5. Experiment with different seeds and prompts
6. Save your favorites and iterate

**Have fun creating artwork for The Genesis Code!**
