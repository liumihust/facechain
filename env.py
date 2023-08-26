import os

APP_PORT_ENV = "APP_PORT"
BASE_MODEL_ENV = "BASE_MODEL"
BASE_MODEL_VERSION_ENV = "BASE_MODEL_VERSION"
BASE_MODEL_SUB_DIR_ENV = "BASE_MODEL_SUB_DIR"
MODEL_PATH_ENV = "MODEL_PATH"
PRE_TRAIN_MODEL_PATH_ENV = "PRE_TRAIN_MODEL_PATH"


server_port = int(os.getenv(APP_PORT_ENV, default="8888"))
base_model = os.getenv(BASE_MODEL_ENV, default='ly261666/cv_portrait_model')
revision = os.getenv(BASE_MODEL_VERSION_ENV)
if revision is None and base_model == 'ly261666/cv_portrait_model':
    revision = 'v4.0'
base_model_sub_dir = os.getenv(BASE_MODEL_SUB_DIR_ENV)
if base_model_sub_dir is None and base_model == 'ly261666/cv_portrait_model':
    base_model_sub_dir = 'film/film'
model_path = os.getenv(MODEL_PATH_ENV, default='/mnt/workspace/.cache/modelscope/')
pretrain_model_path = os.getenv(PRE_TRAIN_MODEL_PATH_ENV, default=model_path + base_model + '/model-resnet_custom_v3.pt')
