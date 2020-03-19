from DOMAIN.business import MyVector
from INFRASTRUCTURE.repository import VectorRepository
from application.controller import  VectorController
from UI.console import VectorUI


v1=MyVector(21,"r",1,[2,40,44,55])
v2=MyVector(2,"y",2,[1,2])
repo=VectorRepository([])
repo.addVector(v1)
repo.addVector(v2)
controller=VectorController(repo)
ui=VectorUI(controller) 
ui.mainMenu()