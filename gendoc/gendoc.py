
"""
Este é um exemplo de arquivo Python para documentação com PyloDe.
Ele inclui imports do PyloDe.
"""

from pylode import OntDoc





od = OntDoc(ontology='../ccso-dbacademic.ttl')

od.make_html(destination=f'../docs/index.html')

