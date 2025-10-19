# Models Installed & Ready to Use

All necessary models have been downloaded and configured for The Genesis Code artwork workflows.

---

## ✅ Installation Summary

### Checkpoint Models (Already Available)
- ✓ **illustriousXL_v01.safetensors** (6.5GB) - For interior sketch drawings
- ✓ **realvisxlV50_v50LightningBakedvae.safetensors** (6.5GB) - For book covers

### LoRA Models
- ✓ **sketch_style_illustrious.safetensors** (218MB) - Sketch style for drawings

### Upscale Models
- ✓ **RealESRGAN_x4plus.pth** (64MB) - 4x upscaling for cover quality

---

## 📂 File Locations

```
~/ComfyUI/
├── models/
│   ├── checkpoints/
│   │   ├── illustriousXL_v01.safetensors ✓
│   │   └── realvisxlV50_v50LightningBakedvae.safetensors ✓
│   ├── loras/
│   │   └── sketch_style_illustrious.safetensors ✓
│   └── upscale_models/
│       └── RealESRGAN_x4plus.pth ✓
└── user/default/workflows/
    ├── comfyui_workflow_book_drawings.json ✓
    ├── comfyui_workflow_book_cover.json ✓
    ├── QUICK_TEST_PROMPTS.txt ✓
    └── GENESIS_CODE_WORKFLOWS_README.txt ✓
```

---

## 🎨 Workflow Configurations

### Interior Drawings Workflow
**File:** `comfyui_workflow_book_drawings.json`

**Configured Settings:**
- Checkpoint: `illustriousXL_v01.safetensors`
- LoRA: `sketch_style_illustrious.safetensors` (strength: 0.85)
- Resolution: 768x1024
- Steps: 25
- CFG Scale: 7.0
- Sampler: euler_ancestral
- Scheduler: normal

**Best For:**
- Simple line art sketches
- Scientific diagrams
- DNA helixes
- Dinosaur illustrations
- Timeline visualizations
- Thought bubbles

---

### Book Cover Workflow
**File:** `comfyui_workflow_book_cover.json`

**Configured Settings:**
- Checkpoint: `realvisxlV50_v50LightningBakedvae.safetensors`
- LoRA: None (disabled, set to 0.0 strength)
- Resolution: 768x1024
- Steps: 30
- CFG Scale: 8.5
- Sampler: dpmpp_2m_sde
- Scheduler: karras
- Upscaler: RealESRGAN x4 (automatic)

**Best For:**
- Bold book covers
- Cinematic sci-fi imagery
- Professional print-quality covers
- Full color dramatic scenes

---

## 🚀 Quick Start

### Step 1: Open ComfyUI
```bash
cd ~/ComfyUI
./start_comfy.sh
```
Then open browser to: http://127.0.0.1:8188

### Step 2: Load a Workflow
- Click "Load" button in ComfyUI
- Navigate to workflows folder
- Select either:
  - `comfyui_workflow_book_drawings.json` OR
  - `comfyui_workflow_book_cover.json`

### Step 3: Use Test Prompts
Open `QUICK_TEST_PROMPTS.txt` for ready-to-use prompts, or see full list in:
`~/projects/genesisBook/EXAMPLE_PROMPTS.md`

### Step 4: Generate
1. Copy a prompt
2. Paste into the positive prompt field (CLIPTextEncode node)
3. Click "Queue Prompt"
4. Wait 20-60 seconds
5. View your generated image!

---

## 💡 Tips for Best Results

### Interior Drawings:
- Keep prompts simple and focused
- Always include "sketch illustration, simple line art"
- Add "black and white" for monochrome results
- Use "minimal shading" for cleaner lines
- Try different seeds for variations

### Book Covers:
- Include color palette suggestions
- Use mood words: "mysterious", "dramatic", "cinematic"
- Specify composition: "centered", "split", "overhead"
- The upscaler automatically creates high-res versions
- Generate multiple variations by changing seed

---

## 🔧 Adjusting Settings

### To Change Image Size:
Find the "EmptyLatentImage" node and modify:
- 768x1024 (current - portrait)
- 1024x768 (landscape)
- 1024x1024 (square)

### To Adjust Quality:
In the "KSampler" node:
- **Steps**: Higher = more detail (20-40 recommended)
- **CFG Scale**: Higher = follows prompt more closely (6-10)
- **Seed**: Change for different variations

### To Adjust Sketch Style:
In the "LoraLoader" node (drawings only):
- Increase to 0.9-1.0 for stronger sketch effect
- Decrease to 0.6-0.7 for subtler sketch lines

---

## 📊 Model Performance

### Expected Generation Times (with GPU):
- Interior drawings: ~20-40 seconds
- Book covers (base): ~30-50 seconds
- Book covers (with upscale): ~60-90 seconds total

### Memory Requirements:
- Drawings: ~8GB VRAM
- Covers: ~8-10GB VRAM
- Both workflows are optimized for consumer GPUs

---

## 🎯 What's Different From Original Plan

**Original Plan:**
- Flux.1 Dev checkpoint (~12GB)
- Specific Flux LoRAs

**What We're Using:**
- IllustriousXL checkpoint (6.5GB) - Works great for sketches
- RealVisXL checkpoint (6.5GB) - Excellent for covers
- Sketch style LoRA from Illustrious family

**Why This Works:**
- Uses models you already had installed
- Saves ~12GB disk space
- SDXL models are mature and proven
- Excellent quality for both sketches and covers
- Faster generation times
- Lower VRAM requirements

---

## 📚 Additional Resources

### In genesisBook project folder:
- `EXAMPLE_PROMPTS.md` - 30+ prompts for different scenes
- `COMFYUI_SETUP_GUIDE.md` - Full setup documentation
- `ARTWORK_README.md` - Complete artwork generation guide
- `GENESIS_CODE_OUTLINE.md` - Book outline for context

### In ComfyUI workflows folder:
- `QUICK_TEST_PROMPTS.txt` - Fast testing prompts
- `GENESIS_CODE_WORKFLOWS_README.txt` - Quick reference

---

## ✨ You're Ready!

Everything is installed and configured. Your workflows are ready to generate artwork for The Genesis Code!

**Next Steps:**
1. Open ComfyUI
2. Load a workflow
3. Try the test prompts
4. Start creating your book artwork!

**Pro Tip:** Generate 10-20 variations of each concept by changing the seed number before committing to a final design. The more you generate, the better your chances of finding the perfect image.

---

**Have fun creating! 🦕🧬✨**
