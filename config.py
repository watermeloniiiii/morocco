root_dir = "/NAS6/Members/linchenxi/projects/morocco"
data_dir = "/NAS6/Members/linchenxi/projects/morocco/data/patch"
local_data_dir = "/media/workspace/linchenxi/.skywalker/cache/patch"
model_dir = "/NAS6/Members/linchenxi/projects/morocco/model"
train_regions = [f"region{i}" for i in [1, 2, 3]]
vali_regions = [f"region{i}" for i in [4]]
test_regions = [f"region{i}" for i in [5, 6, 7]]
mode = "run"
customized_weight = True
encoder_weights = True
class_of_interests = ["negative", "olive"]
STATS_MEAN = [125.60012727962095, 125.66049125060024, 125.5652544331012]
STATS_STD = [53.85292217467926, 55.29551905929324, 56.7204846663869]

viz_param = {
    "CIG": {
        "ylim": (0, 4.6),
        "ylim_ratio": (2, 6),
        "yticks": [0, 1, 2, 3, 4],
        "yticks_ratio": [2, 3, 4, 5, 6],
    },
    "NDVI": {
        "ylim": (0, 0.8),
        "yticks": [0, 0.2, 0.4, 0.6, 0.8],
        "ylim_ratio": (0, 1.5),
        "yticks_ratio": [0, 0.3, 0.6, 0.9, 1.2, 1.5],
    },
    "EVI": {
        "ylim": (-0.2, 0.6),
        "ylim_ratio": (0, 0.8),
        "yticks": [-0.2, 0, 0.2, 0.4, 0.6],
        "yticks_ratio": [0, 0.2, 0.4, 0.6, 0.8],
    },
    "LSWI": {
        "ylim": (-0.4, 0.4),
        "ylim_ratio": (0, 0.6),
        "yticks": [-0.4, -0.2, 0, 0.2, 0.4],
        "yticks_ratio": [0, 0.15, 0.3, 0.45, 0.6],
    },
    "OSAVI": {
        "ylim": (0, 0.6),
        "ylim_ratio": (0, 1),
        "yticks": [0, 0.15, 0.3, 0.45, 0.6],
        "yticks_ratio": [0, 0.25, 0.5, 0.75, 1],
    },
}

cuda = True
model = "unet"
name = f"{model}_19"
if model == "vit":
    general = dict(
        mode="vit",
        optimizer="Adam_StepLR",
        samples="NA",
        # model_index='finetune_200_2',
        model_index="vit_6",
        info="take average after sigmoid/ndvi/cnn with batchnorm and relu",
    )
    hyperparameters = dict(
        bands=3,
        batch_size=16,
        epochs=400,
        SGD_StepLR=dict(lr=1e-4, step_size=20, gamma=0.8, momentum=0.9),
        SGD_CLR=dict(lr=1e-4, max_lr=7e-6, base_lr=5e-7, step_size=20, momentum=0),
        Adam_StepLR=dict(lr=1e-4, step_size=10, gamma=0.5),
        weight_decay=1,
        weight=[1, 4],
        pool="mean",
        image_size=120,
        patch_size=30,
        num_classes=1,
        dim=64,
        depth=5,
        heads=5,
        mlp_dim=1024,
        dropout=0,
        emb_dropout=0,
    )
if model == "unet":
    general = dict(mode="unet", optimizer="AdamW_ONECLR", model_index=name, info="NA")
    hyperparameters = dict(
        bands=3,
        batch_size=256,
        epochs=300,
        SGD_StepLR=dict(lr=1e-4, step_size=5, gamma=0.95, momentum=0),
        SGD_CLR=dict(lr=1e-4, max_lr=5e-5, base_lr=1e-5, step_size=50, momentum=0.9),
        Adam_StepLR=dict(lr=1e-3, step_size=20, gamma=0.95),
        AdamW_ONECLR=dict(lr=1e-4, max_lr=5e-4, pct_start=0.3, div_factor=10),
        hidden_layer=[16, 32, 64, 128],
        weight_decay=5,
        weight=[5, 1],
        dropout=0.3,
    )
if model == "shallow":
    general = dict(mode="shallow", optimizer="", model_index="shallow_32_1", info="NA")
    hyperparameters = dict(
        bands=3,
        batch_size=16,
        epochs=100,
        SGD_StepLR=dict(lr=1e-4, step_size=5, gamma=0.95, momentum=0),
        SGD_CLR=dict(lr=1e-4, max_lr=1e-4, base_lr=7e-5, step_size=15, momentum=0.9),
        Adam_StepLR=dict(lr=3e-5, step_size=10, gamma=0.95),
        AdamW_ONECLR=dict(lr=1e-4, max_lr=1e-4, pct_start=0.2, div_factor=10),
        hidden_layer=[16, 32, 64, 128],
        fc_layer=[128, 128, 256],
        weight_decay=0.1,
        weight=[1, 5],
        dropout=0.3,
    )
if model == "pretrain":
    general = dict(
        mode="pretrain",
        optimizer="SGD_CLR",
        model_index="pretrain_base_16",
        info="1.no adversarial learning, directly take the prob of all sub-patches from ViT\t2.freeze all layers but the last one",
    )
    hyperparameters = dict(
        bands=3,
        batch_size=8,
        epochs=200,
        SGD_StepLR=dict(lr=1e-4, step_size=5, gamma=0.95, momentum=0),
        SGD_CLR=dict(lr=1e-4, max_lr=5e-5, base_lr=2e-5, step_size=15, momentum=0.9),
        Adam_StepLR=dict(lr=1e-4, step_size=20, gamma=0.8),
        weight=[1, 3],
        sub_weight=[1, 1],
        weight_decay=0.6,
        threshold=[0.5, 0.1],
        regularization=60,
    )
