"""
Docstring for tests.test_base
"""


def test_beleza_astride(qualidade:str) -> str:

    qualidades_astride = ["gata","gostosa","bonita"]    
    assert qualidades_astride[2] == qualidade

def test_beleza_elfa(qualidade:str) -> str:
     
     qualidades_elfa = ["linda","doce","carinhosa","bonita"]
     assert qualidades_elfa[3] == qualidade
