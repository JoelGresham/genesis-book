# ComfyUI Setup Guide for The Genesis Code Artwork

This guide will help you set up ComfyUI and download the necessary models to generate artwork for your book.

---

## Prerequisites

- A computer with a decent GPU (NVIDIA recommended with at least 8GB VRAM)
- ~50GB of free disk space for models
- Python 3.10 or newer
- Git installed

---

## Step 1: Install ComfyUI

### Option A: Portable Windows Installation (Easiest)
1. Download ComfyUI portable from: https://github.com/comfyanonymous/ComfyUI/releases
2. Extract the archive
3. Run `run_nvidia_gpu.bat` (or `run_cpu.bat` if no GPU)

### Option B: Manual Installation (All Platforms)
```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt
python main.py
```

### Verify Installation
- ComfyUI should open in your browser at `http://127.0.0.1:8188`
- You should see the default workflow

---

## Step 2: Download Base Models

These are the checkpoint models (large files, ~2-7GB each).

### For Interior Drawings (Choose ONE):

**Option 1: Flux.1 Dev (Recommended)**
- Download: https://huggingface.co/black-forest-labs/FLUX.1-dev
- File: `flux1-dev.safetensors` (~11.9GB)
- Place in: `ComfyUI/models/checkpoints/`

**Option 2: SDXL Base (Alternative)**
- Download: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
- File: `sd_xl_base_1.0.safetensors` (~6.9GB)
- Place in: `ComfyUI/models/checkpoints/`

### For Book Covers (Choose ONE):

**Option 1: DreamShaper XL (Recommended)**
- Download: https://civitai.com/models/112902/dreamshaper-xl
- File: `dreamshaperXL_v21TurboDPMSDE.safetensors` (~6.6GB)
- Place in: `ComfyUI/models/checkpoints/`

**Option 2: Deliberate XL (Alternative)**
- Download: https://civitai.com/models/119057/deliberate-xl
- File: `deliberate_v3.safetensors` (~6.9GB)
- Place in: `ComfyUI/models/checkpoints/`

---

## Step 3: Download LoRA Models

These are style modifiers (smaller files, ~50-300MB each).

### For Interior Drawings:

**Sketch Illustration - Flux (Recommended)**
- Download: https://civitai.com/models/1239147/sketch-illustration
- File: `sketch_illustration_flux.safetensors`
- Place in: `ComfyUI/models/loras/`

**Alternative Options:**
- Pencil Sketch: https://civitai.com/models/55047/pencil-sketch
- Sketch/LineArt: https://civitai.com/models/1298800/sketchlineart

### For Book Covers (Optional but Recommended):

**Book Cover - Flux**
- Download: https://civitai.com/models/793367/book-cover-or-flux
- File: `book_cover_flux.safetensors`
- Place in: `ComfyUI/models/loras/`

---

## Step 4: Download Upscale Model (For Book Covers)

**RealESRGAN x4**
- Download: https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
- File: `RealESRGAN_x4plus.pth` (~64MB)
- Place in: `ComfyUI/models/upscale_models/`

---

## Step 5: Load the Workflows

1. Open ComfyUI in your browser (`http://127.0.0.1:8188`)
2. Click the "Load" button (or drag and drop)
3. Navigate to your `genesisBook` folder
4. Load either:
   - `comfyui_workflow_book_drawings.json` (for interior sketches)
   - `comfyui_workflow_book_cover.json` (for cover designs)

---

## Step 6: Configure the Workflow

### Update Model Names (If Different)

If you downloaded different model files than what's in the workflow:

1. **Find the "CheckpointLoaderSimple" node** (top-left, first node)
2. Click on the model name dropdown
3. Select your downloaded checkpoint model

4. **Find the "LoraLoader" node** (second node)
5. Click on the LoRA name dropdown
6. Select your downloaded LoRA file

### If Models Are Missing:
- The dropdown will show red or empty
- Double-check you placed files in correct folders
- Restart ComfyUI to refresh the model list
- Check that files aren't still downloading

---

## Step 7: Generate Your First Image

1. Copy a prompt from `EXAMPLE_PROMPTS.md`
2. Find the "CLIPTextEncode" node labeled as positive prompt (usually has longer text)
3. Paste your prompt into the text field
4. Click "Queue Prompt" button (top-right)
5. Wait for generation (15-60 seconds depending on your GPU)
6. View the result in the "SaveImage" node

---

## Quick Reference: Folder Structure

```
ComfyUI/
├── models/
│   ├── checkpoints/          # Put .safetensors checkpoint models here
│   │   ├── flux1-dev.safetensors
│   │   └── dreamshaperXL_v21TurboDPMSDE.safetensors
│   ├── loras/                # Put LoRA files here
│   │   ├── sketch_illustration_flux.safetensors
│   │   └── book_cover_flux.safetensors
│   └── upscale_models/       # Put upscaler models here
│       └── RealESRGAN_x4plus.pth
└── output/                   # Generated images save here automatically
```

---

## Troubleshooting

### Error: "Out of Memory"
- Reduce image resolution in "EmptyLatentImage" node (try 512x768)
- Close other GPU-intensive applications
- Use lower precision models if available
- Consider using CPU mode (much slower)

### Error: "Model not found"
- Verify file is in correct folder
- Restart ComfyUI to refresh model list
- Check filename matches exactly (case-sensitive)
- Ensure download completed fully

### Error: "CUDA out of memory" or "Not enough VRAM"
- Use smaller batch size (set to 1 in EmptyLatentImage)
- Lower the resolution
- Close other programs using GPU
- Try SDXL models instead of Flux (lower VRAM requirements)

### Generation is Very Slow
- Normal for CPU generation (can take 5-15 minutes)
- GPU generation should be 15-60 seconds
- Verify ComfyUI is using your GPU (check console output)
- First generation is always slower (model loading)

### Colors Look Wrong in Sketches
- Interior drawings should be black and white
- Check negative prompt includes "color"
- Increase LoRA strength (try 0.9-1.0)
- Adjust CFG scale (try 6-7)

### Cover Looks Too Busy/Cluttered
- Simplify your prompt (remove some descriptors)
- Add more negative prompts: "cluttered, busy, chaotic"
- Lower the CFG scale (try 7.0-7.5)
- Try different seeds

---

## Performance Expectations

### GPU Performance (NVIDIA RTX 3060 or better):
- Interior drawings: 15-30 seconds
- Book covers: 30-60 seconds
- Upscaling: 10-20 seconds additional

### GPU Performance (Lower-end):
- Interior drawings: 30-90 seconds
- Book covers: 60-180 seconds
- May need to reduce resolution

### CPU Performance:
- Interior drawings: 5-15 minutes
- Book covers: 10-30 minutes
- Upscaling: 5-10 minutes
- Not recommended for iterative work

---

## Next Steps

1. ✅ Install ComfyUI
2. ✅ Download checkpoint models
3. ✅ Download LoRA models
4. ✅ Download upscale model
5. ✅ Load workflow
6. ✅ Test with a simple prompt
7. 🎨 Start creating your book artwork!

---

## Recommended Workflow Process

### For Interior Drawings:
1. Start with simple prompts from `EXAMPLE_PROMPTS.md`
2. Generate 5-10 variations (change seed each time)
3. Pick your favorites
4. Refine the prompt for selected styles
5. Generate finals at higher resolution if needed
6. Clean up in image editor if necessary (remove artifacts)

### For Book Covers:
1. Try multiple concept prompts (try all 10 from examples)
2. Generate 3-5 variations of favorites
3. Use the upscaled versions for evaluation
4. Combine elements in Photoshop/GIMP if needed
5. Add title text and author name in separate software
6. Export at print resolution (300 DPI minimum)

---

## Additional Resources

- **ComfyUI Documentation**: https://docs.comfy.org/
- **CivitAI Model Library**: https://civitai.com/
- **ComfyUI Community**: https://reddit.com/r/comfyui
- **Flux Model Documentation**: https://huggingface.co/black-forest-labs
- **Prompt Engineering Guide**: https://platform.openai.com/docs/guides/prompt-engineering

---

## Model License Notes

**Important**: Review the license for each model you download:
- **Flux.1 Dev**: Non-commercial use only (check license for commercial use)
- **SDXL**: CreativeML Open RAIL++-M License (commercial allowed with restrictions)
- **DreamShaper XL**: Check specific version license on CivitAI
- **LoRAs**: Vary by creator - always check the model page

For commercial book publication, ensure you have the right to use the models commercially. Some may require attribution or have restrictions.

---

## Recommended Settings Summary

### Interior Drawings Workflow:
- **Model**: Flux.1 Dev
- **LoRA**: Sketch Illustration (strength: 0.85)
- **Resolution**: 768x1024
- **Steps**: 25
- **CFG**: 7.0
- **Sampler**: euler_ancestral
- **Scheduler**: normal

### Book Cover Workflow:
- **Model**: DreamShaper XL
- **LoRA**: Book Cover Flux (strength: 0.75)
- **Resolution**: 768x1024
- **Steps**: 30
- **CFG**: 8.5
- **Sampler**: dpmpp_2m_sde
- **Scheduler**: karras
- **Upscale**: Yes (RealESRGAN x4)

---

**You're now ready to create stunning artwork for The Genesis Code!**

Happy generating! 🎨🦕🧬
