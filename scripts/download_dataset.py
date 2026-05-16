import kagglehub

print("Downloading dataset...")

path = kagglehub.dataset_download("sumeakash/ai-impact-on-job-sector", output_dir="../dataset", force_download=True)

print("Dataset downloaded to:", path)