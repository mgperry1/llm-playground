from fastai.vision.all import *

# path = untar_data(URLs.PETS)
# dls = ImageDataLoaders.from_name_re(path, get_image_files(path/'images'), pat='(.+)_\d+.jpg', item_tfms=Resize(460), batch_tfms=aug_transforms(size=224, min_scale=0.75))
# learn = vision_learner(dls, models.resnet50, metrics=accuracy)
# learn.fine_tune(1)
# learn.path = Path('.')
# learn.export()


path = Path("/home/mgp17171/repos/llm-playground/fastai")
path.ls(file_exts=".pkl")
learn = load_learner(path / "bikemodel.pkl")
labels = learn.dls.vocab


def predict(img):
    img = PILImage.create(img)
    pred, pred_idx, probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}


results = learn.predict(path / "moutain.jpeg")
print(results)
predict(path / "moutain.jpeg")
