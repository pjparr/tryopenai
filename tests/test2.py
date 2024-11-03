# from huggingface_hub import HfApi, ModelFilter

# api = HfApi()
# models = api.list_models(filter=ModelFilter(task="automatic-speech-recognition"))
# models = list(models)
# print(len(models))
# print(models[0].modelId)

from huggingface_hub import list_models

for model in list_models(
    limit=10, sort="downloads", direction=-1, filter="text-to-image"
):
    print(model.id, model.downloads)
