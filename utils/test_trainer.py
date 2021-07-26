from utils.trainer_utils import TrainConfig
from flearn.trainer.fedavg import FedAvg
from flearn.trainer.fesem import FeSEM
from flearn.trainer.fedgroup import FedGroup
from flearn.trainer.ifca import IFCA

def main():
    config = TrainConfig('femnist', 'mclr', 'fedgroup')
    config.trainer_config['dynamic'] = True
    config.trainer_config['swap_p'] = 0.02
    config.client_config['temperature'] = 3
    config.trainer_config['temp_metrics'] = 'l2'
    config.trainer_config['temp_func'] = 'linear'
    trainer = FedGroup(config)
    trainer.train()
    #trainer.train_locally()

main()