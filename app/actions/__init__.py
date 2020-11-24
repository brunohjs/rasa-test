#########################
# Bibliotecas para o RASA
from sys import path
path.append(".")

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from . import *

#########################
# Outras bibliotecas
import random
from helpers import utils, Sender

#########################
# Scripts que serão executados ao iniciar o servidor de ações
from scripts.cleanModels import *
#########################