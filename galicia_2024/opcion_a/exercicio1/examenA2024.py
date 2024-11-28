class CicloFormativo: 
    def __init__(self, nome_ciclo, familia_profesional, grao): 
        """  Inicializa unha nova instancia de CicloFormativo. 
        :param nome_ciclo: Nome do ciclo formativo. 
        :param familia: Familia profesional do ciclo formativo. 
        :param grao: Grao do ciclo (básico, medio, superior ou curso 
        especialización).""" 
        self.nome_ciclo = nome_ciclo 
        self.familia_profesional = familia_profesional 
        self.grao = grao 
    def __str__(self): 
        """ Devolve unha representación en cadea do ciclo formativo. """ 
        return f"{self.nome_ciclo} ({self.familia_profesional}, {self.grao})"
    
    
class CentroEducativo: 
    def __init__(self, nome_centro, provincia, concello, ciclo_formativo, prazas): 
        """ Inicializa unha nova instancia de CentroEducativo. 
        :param nome: Nome do centro educativo. 
        :param provincia: Provincia na que se atopa o centro. 
        :param concello: Concello no que se atopa o centro. 
        :param ciclo_formativo: Instancia de CicloFormativo ofrecida polo centro. 
        :param prazas: Número de prazas ofertadas. """ 
        self.nome_centro = nome_centro 
        self.provincia = provincia 
        self.concello = concello 
        self.ciclo_formativo: CicloFormativo = ciclo_formativo 
        self.prazas = prazas 
    def __str__(self): 
        """ Devolve unha representación en cadea do centro educativo. """ 
        return f"{self.nome_centro} - {self.provincia} - {self.concello} - {self.ciclo_formativo} - {self.prazas} prazas"
        
        
class XestionFP: 
    def __init__(self): 
        """  Inicializa unha nova instancia de XestionFP.  """ 
        self.centros: list[CentroEducativo] = [] 
        
    def engadir_centro(self, centro): 
        """  Engade un centro educativo á lista de centros. 
        :param centro: Instancia de CentroEducativo a engadir.  """ 
        self.centros.append(centro) 
        print(f"Centro engadido: {centro}") 
        
    def listar_centros(self): 
        """  Imprime por pantalla todos os centros educativos  """
        for x in self.centros:
            print(x)
        
    def buscar_por_concello(self, concello): 
        """  Busca centros educativos nun concello específico. 
        :param concello: Nome do concello. 
        :return: Lista de centros educativos no concello especificado
        """
        encontrados = []
        for x in self.centros:
            if x.concello == concello:
                encontrados.append(x)
        return encontrados
                

    def prazas_por_familia(self): 
        """  Calcula o número total de prazas ofertadas por cada familia 
        profesional. 
        :return: Dicionario coa familia profesional como clave e o número de prazas 
        como valor.""" 
        prazas_familia = {}
        
        for x in self.centros:
            familia = x.ciclo_formativo.familia_profesional
            if familia not in prazas_familia:
                prazas_familia[familia] = 0
            prazas_familia[familia] += x.prazas
            
        return prazas_familia
    
    
if __name__ == '__main__': 
    #Creamos la instancia de XestionFP
    xestion = XestionFP()
    
    # Engadir ciclos formativos de exemplo 
    dam = CicloFormativo("Desenvolvemento de Aplicacións Multiplataforma", "Informática", "Grao Superior")
    xestAdmin = CicloFormativo("Xestión Administrativa", "Administración", "Grao Medio")
    ifc = CicloFormativo("Informática e Comunicacións", "Informática", "Grao Básico")
    
    
    # Engadir centros educativos de exemplo 
    xestion.engadir_centro(CentroEducativo("Centro A","A Coruña", "Ribeira", dam, 30))    
    xestion.engadir_centro(CentroEducativo("Centro B", "A Coruña", "Santiago de Compostela", xestAdmin, 60))    
    xestion.engadir_centro(CentroEducativo("Centro A", "A Coruña","Ribeira", ifc, 30))
    #Centro C co ciclo dam
    xestion.engadir_centro(CentroEducativo("Centro C","Ourense", "Ourense", dam, 60))
    
    # Listar todos os centros educativos 
    print("\nLISTA DE CENTROS")
    xestion.listar_centros()
    
    # Solicitar un concello por teclado e buscar centros por concello 
    concello = input("\nIntroduce o concello para a busqueda de centros: ")
    lista_centros = xestion.buscar_por_concello(concello)
    for centro in lista_centros: print(centro)
    
    # Buscar prazas ofertadas por familia profesional 
    print("\nPRAZAS OFERTADAS POR FAMILIA PROFESIONAL")
    print(xestion.prazas_por_familia())