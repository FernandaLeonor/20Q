def validar_respuesta(prompt, contador):
    """Valida que la respuesta sea 'sí' o 'no'"""
    while True:
        if contador > 0: 
            respuesta = input(f"{contador}. {prompt}").strip().lower()
        else:
            respuesta = input(prompt).strip().lower()
        if respuesta in ['sí', 'si', 's', 'no', 'n']:
            return 'sí' if respuesta in ['sí', 'si', 's'] else 'no'
        print("Por favor, responde con 'sí' o 'no'.")


def jugar_una_partida():
    """Ejecuta una partida del juego"""
    print("\n" + "="*50)
    print("¡Bienvenido al juego de las 20 preguntas!")
    print("Piensa en un objeto y responderé con preguntas que solo puedes")
    print("contestar con 'sí' o 'no'.")
    print("="*50 + "\n")

    contador_preguntas = 0
    
    def hacer_pregunta(pregunta):
        nonlocal contador_preguntas
        if contador_preguntas >= 20:
            print("\n😔 No pude adivinar en lo que estabas pensando en 20 preguntas.")
            return None
        contador_preguntas += 1
        return validar_respuesta(pregunta, contador_preguntas)
    
    respuesta = hacer_pregunta("¿Es tangible? (sí/no) ")
    if respuesta is None: return False

    if respuesta == "sí":
        respuesta = hacer_pregunta("¿Es un ser vivo? (sí/no) ")
        if respuesta is None: return False
        
        if respuesta == "sí":
            respuesta = hacer_pregunta("¿Pertenece al reino animal? (sí/no) ")
            if respuesta is None: return False
            
            if respuesta == "sí":
                respuesta = hacer_pregunta("¿Es vertebrado? (sí/no) ")
                if respuesta is None: return False
                
                if respuesta == "sí":
                    respuesta = hacer_pregunta("¿Es un humano? (sí/no) ")
                    if respuesta is None: return False
                    
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Es un hombre? (sí/no) ")
                        if respuesta is None: return False
                        
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es una persona famosa? (sí/no) ")
                            if respuesta is None: return False
                            
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es un deportista? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🏅 Estabas pensando en un deportista famoso.")
                                    return True
                                respuesta = hacer_pregunta("¿Es un músico? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🎸 Estabas pensando en un músico famoso.")
                                    return True
                                respuesta = hacer_pregunta("¿Es un cantante? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🎤 Estabas pensando en un cantante famoso.")
                                    return True
                                respuesta = hacer_pregunta("¿Es un actor? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🎭 Estabas pensando en un actor famoso.")
                                    return True
                                respuesta = hacer_pregunta("¿Es un científico? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🔬 Estabas pensando en un científico famoso.")
                                    return True
                                respuesta = hacer_pregunta("¿Es un político? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🏛️ Estabas pensando en un político famoso.")
                                    return True
                                respuesta = hacer_pregunta("¿Es un empresario? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 👔 Estabas pensando en un empresario famoso.")
                                    return True
                            else:
                                print("¡Adiviné! 👨 Estabas pensando en un hombre común.")
                                return True
                        else:
                            respuesta = hacer_pregunta("¿Es una persona famosa? (sí/no) ")
                            if respuesta is None: return False
                            
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es una deportista? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🏅 Estabas pensando en una deportista famosa.")
                                    return True
                                respuesta = hacer_pregunta("¿Es una cantante? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🎤 Estabas pensando en una cantante famosa.")
                                    return True
                                respuesta = hacer_pregunta("¿Es una actriz? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🎭 Estabas pensando en una actriz famosa.")
                                    return True
                                respuesta = hacer_pregunta("¿Es una científica? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🔬 Estabas pensando en una científica famosa.")
                                    return True
                                respuesta = hacer_pregunta("¿Es una política? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 🏛️ Estabas pensando en una política famosa.")
                                    return True
                                respuesta = hacer_pregunta("¿Es una empresaria? (sí/no) ")
                                if respuesta == "sí":
                                    print("¡Adiviné! 👔 Estabas pensando en una empresaria famoso.")
                                    return True
                            else:
                                print("¡Adiviné! 👩 Estabas pensando en una mujer común.")
                                return True
                    else:
                        respuesta = hacer_pregunta("¿Es un mamífero? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es terrestre? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es doméstico? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Es un animal de compañía? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un perro o un gato.")
                                        return True
                                    else:
                                        respuesta = hacer_pregunta("¿Se cría para consumo humano? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser una vaca, cerdo o caballo.")
                                            return True
                                        else:
                                            print("Puede ser una llama o alpaca.")
                                            return True
                                else:
                                    respuesta = hacer_pregunta("¿Tiene bolsa para sus crías? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un canguro, koala o una zarigüeya.")
                                    else:
                                        respuesta = hacer_pregunta("¿Es un carnívoro? (sí/no) ")
                                        if respuesta == "sí":
                                            respuesta = hacer_pregunta("¿Caza en grupo? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser un león, tigre o lobo.")
                                                return True
                                            else:
                                                respuesta = hacer_pregunta("¿Es un felino? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser un tigre o un jaguar.")
                                                    return True
                                                else:
                                                    print("Puede ser un oso o un zorro.")
                                                    return True
                                        else:
                                            respuesta = hacer_pregunta("¿Es un herbívoro? (sí/no) ")
                                            if respuesta == "sí":
                                                respuesta = hacer_pregunta("¿Tiene cuernos? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser un ciervo o un búfalo.")
                                                    return True
                                                else:
                                                    print("Puede ser un elefante o una jirafa.")
                                                    return True
                                            else:
                                                respuesta = hacer_pregunta("¿Se alimenta de carroña? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser una hiena o un buitre.")
                                                    return True
                            else:
                                respuesta = hacer_pregunta("¿Es marino? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Tiene aletas? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un delfín o una ballena.")
                                        return True
                                    else:
                                        respuesta = hacer_pregunta("¿Tiene bigotes? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser una foca o una morsa.")
                                            return True
                                        else:
                                            print("Puede ser un hipopótamo o una nutria.")
                                            return True
                                else:
                                    respuesta = hacer_pregunta("¿Es volador? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un murciélago.")
                                        return True
                        else:
                            respuesta = hacer_pregunta("¿Es un ave? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Pone huevos? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Es rapaz? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un águila, un halcón o un búho.")
                                        return True
                                    else:
                                        respuesta = hacer_pregunta("¿Nada y se desplaza bien en el agua? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser un pato o un pingüino.")
                                            return True
                                        else:
                                            respuesta = hacer_pregunta("¿Es un ave canora? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser un ruiseñor o un canario.")
                                                return True
                                            else:
                                                print("Puede ser una paloma o un loro.")
                                                return True
                            else:
                                respuesta = hacer_pregunta("¿Es un reptil? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Tiene caparazón? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser una tortuga.")
                                        return True
                                    else:
                                        respuesta = hacer_pregunta("¿Es acuático? (sí/no" )
                                        if respuesta == "sí":
                                            print("Puede ser un cocodrilo.")
                                            return True
                                        else:
                                            respuesta = hacer_pregunta("¿Tiene patas? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser un lagarto o un camaleón.")
                                                return True
                                            else:
                                                print("Puede ser una víbora, serpiente o una pitón.")
                                                return True
                                else:
                                    respuesta = hacer_pregunta("¿Es un pez? (sí/no) ")
                                    if respuesta == "sí":
                                        respuesta = hacer_pregunta("¿Es de agua dulce? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser una trucha o un bagre.")
                                            return True
                                        else:
                                            print("Puede ser un atún o una sardina.")
                                            return True
                                    else:
                                        respuesta = hacer_pregunta("¿Es un anfibio? (sí/no) ")
                                        if respuesta == "sí":
                                            respuesta = hacer_pregunta("¿Salta? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser una rana o un sapo.")
                                                return True
                                            else:
                                                print("Puede ser un ajolote o una salamandra.")
                                                return True
                else:
                    respuesta = hacer_pregunta("¿Es un insecto? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Tiene alas? (sí/no) ")
                        if respuesta == "sí":
                            print("Puede ser una mariposa, una libélula o un mosquito.")
                            return True
                        else:
                            respuesta = hacer_pregunta("¿Salta? (sí/no) ")
                            if respuesta == "sí":
                                print("Puede ser un grillo o una langosta.")
                                return True
                            else:
                                print("Puede ser una hormiga o una cucaracha.")
                                return True
                    else:
                        respuesta = hacer_pregunta("¿Es un arácnido? (sí/no) ")
                        if respuesta == "sí":
                            print("Puede ser una araña o un escorpión.")
                            return True
                        else:
                            respuesta = hacer_pregunta("¿Es un molusco? (sí/no) ")
                            if respuesta == "sí":
                                print("Puede ser un caracol o una almeja.")
                                return True
                            else:
                                respuesta = hacer_pregunta("¿Es un equinodermo? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser una estrella de mar o un erizo de mar.")
                                    return True
                                else:
                                    print("Puede ser un cnidario como una medusa o un coral.")
                                    return True
            else:
                respuesta = hacer_pregunta("¿Es una planta? (sí/no) ")
                if respuesta == "sí":
                    respuesta = hacer_pregunta("¿Tiene flores? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Produce frutos? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es un árbol? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿El fruto es carnoso? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser un manzano o un peral.")
                                    return True
                                else:
                                    print("Puede ser un nogal o un almendro.")
                                    return True
                            else:
                                respuesta = hacer_pregunta("¿Es una planta ornamental? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser una rosa o un tulipán.")
                                    return True
                                else:
                                    print("Puede ser una lavanda o un girasol.")
                                    return True
                        else:
                            print("Es una planta con flores pero sin frutos, como una margarita.")
                            return True
                    else:
                        respuesta = hacer_pregunta("¿Es un helecho? (sí/no) ")
                        if respuesta == "sí":
                            print("Es un helecho.")
                            return True
                        else:
                            print("Es un musgo.")
                            return True
                else:
                    respuesta = hacer_pregunta("¿Es un hongo? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Es comestible? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Se usa en cocina? (sí/no) ")
                            if respuesta == "sí":
                                print("Es un champiñón.")
                                return True
                            else:
                                print("Es una trufa.")
                                return True
                        else:
                            respuesta = hacer_pregunta("¿Es venenoso? (sí/no) ")
                            if respuesta == "sí":
                                print("Es una amanita muscaria.")
                                return True
                            else:
                                print("Es un moho.")
                                return True
                    else:
                        respuesta = hacer_pregunta("¿Es un microorganismo? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es una bacteria? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Causa enfermedades? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser una bacteria patógena como E. coli.")
                                    return True
                                else:
                                    print("Puede ser una bacteria benéfica como Lactobacillus.")
                                    return True
                            else:
                                respuesta = hacer_pregunta("¿Es un virus? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Afecta a humanos? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser el virus de la gripe o COVID-19.")
                                        return True
                                    else:
                                        print("Puede ser un virus vegetal o animal.")
                                        return True
                                else:
                                    respuesta = hacer_pregunta("¿Es un protozoo? (sí/no) ")
                                    if respuesta == "sí":
                                        respuesta = hacer_pregunta("¿Causa enfermedades? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser un parásito como la malaria.")
                                            return True
                                        else:
                                            print("Puede ser un protozoo de vida libre.")
                                            return True
        else:
            respuesta = hacer_pregunta("¿Es algo natural? (sí/no) ")
            if respuesta == "sí":
                respuesta = hacer_pregunta("¿Es un fenómeno? (sí/no) ")
                if respuesta == "sí":
                    respuesta = hacer_pregunta("¿Es un fenómeno atmosférico? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Está relacionado con la precipitación? (sí/no) ")
                        if respuesta == "sí":
                            print("Puede ser lluvia, nieve o granizo.")
                            return True
                        else:
                            respuesta = hacer_pregunta("¿Es un fenómeno extremo? (sí/no) ")
                            if respuesta == "sí":
                                print("Puede ser un huracán, tornado o ventisca.")
                                return True
                            else:
                                print("Puede ser un arcoíris o una niebla.")
                                return True
                    else:
                        respuesta = hacer_pregunta("¿Es un fenómeno geológico? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es causado por la actividad sísmica? (sí/no) ")
                            if respuesta == "sí":
                                print("Puede ser un terremoto o un tsunami.")
                                return True
                            else:
                                respuesta = hacer_pregunta("¿Involucra magma o fuego? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser una erupción volcánica.")
                                    return True
                                else:
                                    print("Puede ser erosión o formación de montañas.")
                                    return True
                        else:
                            respuesta = hacer_pregunta("¿Es un fenómeno astronómico? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Ocurre en la atmósfera terrestre? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser una aurora boreal.")
                                    return True
                                else:
                                    respuesta = hacer_pregunta("¿Involucra cuerpos celestes? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un eclipse, un meteorito o un cometa.")
                                        return True
                            else:
                                respuesta = hacer_pregunta("¿Es un fenómeno físico-químico? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Está relacionado con la energía? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un rayo, una onda de calor o una congelación extrema.")
                                        return True
                                    else:
                                        print("Puede ser magnetismo, gravedad o una reacción química natural.")
                                        return True
                else:
                    respuesta = hacer_pregunta("¿Es un material? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Es un mineral? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es un mineral precioso? (sí/no) ")
                            if respuesta == "sí":
                                print("Puede ser diamante, esmeralda o rubí.")
                                return True
                            else:
                                print("Puede ser cuarzo, feldespato o mica.")
                                return True
                        else:
                            respuesta = hacer_pregunta("¿Es una roca? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es una roca ígnea? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser granito, basalto o pumita.")
                                    return True
                                else:
                                    respuesta = hacer_pregunta("¿Es una roca sedimentaria? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser arenisca, caliza o conglomerado.")
                                        return True
                                    else:
                                        print("Puede ser una roca metamórfica como mármol o pizarra.")
                                        return True
                            else:
                                respuesta = hacer_pregunta("¿Es un metal? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser oro, cobre, hierro o aluminio.")
                                    return True
                                else:
                                    respuesta = hacer_pregunta("¿Es un gas natural? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser oxígeno, nitrógeno o dióxido de carbono.")
                                        return True
                    else:
                        respuesta = hacer_pregunta("¿Es una formación? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es una formación geológica? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es una montaña? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser el Everest, el Aconcagua o el Kilimanjaro.")
                                    return True
                                else:
                                    respuesta = hacer_pregunta("¿Es una cueva o cañón? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser la Cueva de los Cristales o el Gran Cañón.")
                                        return True
                                    else:
                                        print("Puede ser una meseta o una llanura.")
                                        return True
                            else:
                                respuesta = hacer_pregunta("¿Es un cuerpo de agua? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Es agua dulce? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un río, un lago o una laguna.")
                                        return True
                                    else:
                                        print("Puede ser un océano o un mar.")
                                        return True
            else:
                respuesta = hacer_pregunta("¿Es una herramienta? (sí/no) ")
                if respuesta == "sí":
                    respuesta = hacer_pregunta("¿Es eléctrica? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Sirve para cortar o perforar? (sí/no) ")
                        if respuesta == "sí":
                            print("Puede ser un taladro, una sierra eléctrica o una lijadora.")
                            return True
                        else:
                            print("Puede ser una aspiradora, una bomba de aire o una batidora.")
                            return True
                    else:
                        respuesta = hacer_pregunta("¿Es analógica? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Sirve para sujetar o ajustar? (sí/no) ")
                            if respuesta == "sí":
                                print("Puede ser una llave inglesa, una prensa o un tornillo de banco.")
                                return True
                            else:
                                print("Puede ser un martillo, un destornillador o una llave de tuercas.")
                                return True
                        else:
                            respuesta = hacer_pregunta("¿Es digital? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Tiene una pantalla o interfaz digital? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser un multímetro, una báscula digital o un calibrador láser.")
                                    return True
                                else:
                                    print("Puede ser un software de diseño, un simulador o una herramienta de modelado digital.")
                                    return True
                else:
                    respuesta = hacer_pregunta("¿Es un medio de transporte? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Se desplaza por tierra? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es un vehículo con motor? (sí/no) ")
                            if respuesta == "sí":
                                print("Puede ser un automóvil, una motocicleta, un autobús o un camión.")
                                return True
                            else:
                                print("Puede ser una bicicleta, un patinete o una carreta.")
                                return True
                        else:
                            respuesta = hacer_pregunta("¿Se desplaza por aire? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es una aeronave de ala fija? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser un avión o un planeador.")
                                    return True
                                else:
                                    print("Puede ser un helicóptero o un dron.")
                                    return True
                            else:
                                respuesta = hacer_pregunta("¿Se desplaza por agua? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Es una embarcación de gran tamaño? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un barco de carga, un crucero o un transatlántico.")
                                        return True
                                    else:
                                        print("Puede ser una lancha, un velero o una canoa.")
                                        return True
                    else:
                        respuesta = hacer_pregunta("¿Es un aparato electrónico? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Se usa para comunicación? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es un dispositivo móvil? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser un teléfono celular o una tableta.")
                                    return True
                                else:
                                    print("Puede ser un teléfono fijo, un radio o un intercomunicador.")
                                    return True
                            else:
                                respuesta = hacer_pregunta("¿Se usa para entretenimiento? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Es un dispositivo de audio o video? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser una televisión, una bocina o una consola de videojuegos.")
                                        return True
                                    else:
                                        print("Puede ser un proyector o un reproductor multimedia.")
                                        return True
                                else:
                                    respuesta = hacer_pregunta("¿Es un dispositivo de computación? (sí/no) ")
                                    if respuesta == "sí":
                                        respuesta = hacer_pregunta("¿Es un equipo portátil? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser una laptop, una tableta o un smartwatch.")
                                            return True
                                        else:
                                            print("Puede ser una computadora de escritorio o un servidor.")
                                            return True
                                    else:
                                        respuesta = hacer_pregunta("¿Es un electrodoméstico? (sí/no) ")
                                        if respuesta == "sí":
                                            respuesta = hacer_pregunta("¿Se usa en la cocina? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser un refrigerador, un microondas o una licuadora.")
                                                return True
                                            else:
                                                print("Puede ser una lavadora, un aire acondicionado o una aspiradora.")
                                                return True
                        else:
                            respuesta = hacer_pregunta("¿Es un mobiliario? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es para el hogar? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Es para la sala o recámara? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser un sofá, una cama o un sillón.")
                                        return True
                                    else:
                                        print("Puede ser un comedor, una mesa o una silla.")
                                        return True
                                else:
                                    respuesta = hacer_pregunta("¿Es para oficina? (sí/no) ")
                                    if respuesta == "sí":
                                        respuesta = hacer_pregunta("¿Es para trabajo o almacenamiento? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser un escritorio o una silla de oficina.")
                                            return True
                                        else:
                                            print("Puede ser un archivero o una estantería.")
                                            return True
                                    else:
                                        respuesta = hacer_pregunta("¿Es para exteriores? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser un banco, una mesa de jardín o una sombrilla.")
                                            return True
                                        else:
                                            respuesta = hacer_pregunta("¿Es para almacenamiento? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser un armario, una repisa o un baúl.")
                                                return True
                            else:
                                respuesta = hacer_pregunta("¿Es una prenda? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Se usa en la parte superior del cuerpo? (sí/no) ")
                                    if respuesta == "sí":
                                        respuesta = hacer_pregunta("¿Es de uso formal? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser una camisa, una blusa o un saco.")
                                            return True
                                        else:
                                            print("Puede ser una playera, un suéter o una chaqueta.")
                                            return True
                                    else:
                                        respuesta = hacer_pregunta("¿Se usa en la parte inferior del cuerpo? (sí/no) ")
                                        if respuesta == "sí":
                                            respuesta = hacer_pregunta("¿Es una prenda exterior? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser un pantalón, una falda o un short.")
                                                return True
                                            else:
                                                print("Puede ser ropa interior como calzones o bóxers.")
                                                return True
                                        else:
                                            respuesta = hacer_pregunta("¿Es un calzado? (sí/no) ")
                                            if respuesta == "sí":
                                                respuesta = hacer_pregunta("¿Es deportivo? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser un tenis o un zapato deportivo.")
                                                    return True
                                                else:
                                                    print("Puede ser un zapato formal, sandalia o bota.")
                                                    return True
                                            else:
                                                respuesta = hacer_pregunta("¿Es un accesorio? (sí/no) ")
                                                if respuesta == "sí":
                                                    respuesta = hacer_pregunta("¿Se usa en la cabeza? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser un gorro, una gorra o un sombrero.")
                                                        return True
                                                    else:
                                                        print("Puede ser un cinturón, una bufanda o unos guantes.")
                                                        return True
                                else:
                                    respuesta = hacer_pregunta("¿Es un alimento? (sí/no) ")
                                    if respuesta == "sí":
                                        respuesta = hacer_pregunta("¿Es de origen animal? (sí/no) ")
                                        if respuesta == "sí":
                                            respuesta = hacer_pregunta("¿Es carne? (sí/no) ")
                                            if respuesta == "sí":
                                                respuesta = hacer_pregunta("¿Proviene de tierra? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser carne de res, cerdo o pollo.")
                                                    return True
                                                else:
                                                    print("Puede ser pescado o mariscos.")
                                                    return True
                                            else:
                                                respuesta = hacer_pregunta("¿Es un producto derivado? (sí/no) ")
                                                if respuesta == "sí":
                                                    respuesta = hacer_pregunta("¿Es un lácteo? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser leche, queso o yogur.")
                                                        return True
                                                    else:
                                                        print("Puede ser huevo o miel.")
                                                        return True
                                        else:
                                            respuesta = hacer_pregunta("¿Es de origen vegetal? (sí/no) ")
                                            if respuesta == "sí":
                                                respuesta = hacer_pregunta("¿Es una fruta? (sí/no) ")
                                                if respuesta == "sí":
                                                    respuesta = hacer_pregunta("¿Es cítrica? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser naranja, limón o toronja.")
                                                        return True
                                                    else:
                                                        print("Puede ser manzana, plátano o uva.")
                                                        return True
                                                else:
                                                    respuesta = hacer_pregunta("¿Es de hoja verde? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser lechuga, espinaca o acelga.")
                                                        return True
                                                    else:
                                                        print("Puede ser zanahoria, papa o jitomate.")
                                                        return True
                                            else:
                                                respuesta = hacer_pregunta("¿Es un grano o cereal? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser arroz, trigo, maíz o avena.")
                                                    return True
                                                else:
                                                    respuesta = hacer_pregunta("¿Es un alimento procesado? (sí/no) ")
                                                    if respuesta == "sí":
                                                        respuesta = hacer_pregunta("¿Es dulce? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser un chocolate, caramelo o pastel.")
                                                            return True
                                                        else:
                                                            print("Puede ser pan, galletas o embutidos.")
                                                            return True
                                    else:
                                        respuesta = hacer_pregunta("¿Es una bebida? (sí/no) ")
                                        if respuesta == "sí":
                                            respuesta = hacer_pregunta("¿Contiene alcohol? (sí/no) ")
                                            if respuesta == "sí":
                                                respuesta = hacer_pregunta("¿Es fermentada? (sí/no) ")
                                                if respuesta == "sí":
                                                    respuesta = hacer_pregunta("¿Proviene de uva? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser vino.")
                                                        return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Proviene de cebada? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser cerveza.")
                                                            return True
                                                        else:
                                                            print("Puede ser sake.")
                                                            return True
                                                else:
                                                    respuesta = hacer_pregunta("¿Proviene de caña de azúcar? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser ron.")
                                                        return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Proviene de uva? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser brandy o coñac.")
                                                            return True
                                                        else:
                                                            print("Puede ser whisky o tequila.")
                                                            return True
                                            else:
                                                respuesta = hacer_pregunta("¿Se consume caliente? (sí/no) ")
                                                if respuesta == "sí":
                                                    respuesta = hacer_pregunta("¿Contiene cafeína? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser café o té negro.")
                                                        return True
                                                    else:
                                                        print("Puede ser té de hierbas, chocolate caliente o infusión.")
                                                        return True
                                                else:
                                                    respuesta = hacer_pregunta("¿Es carbonatada? (sí/no) ")
                                                    if respuesta == "no":
                                                        respuesta = hacer_pregunta("¿Proviene de fruta? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser jugo de naranja, manzana o piña.")
                                                            return True
                                                        else:
                                                            print("Puede ser leche.")
                                                            return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Tiene azúcar? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser refresco o bebida energética.")
                                                            return True
                                                        else:
                                                            print("Puede ser agua mineral o soda.")
                                                            return True
                                        else:
                                            respuesta = hacer_pregunta("¿Es un utensilio? (sí/no) ")
                                            if respuesta == "sí":
                                                respuesta = hacer_pregunta("¿Se usa en la cocina? (sí/no) ")
                                                if respuesta == "sí":
                                                    respuesta = hacer_pregunta("¿Se usa para preparar alimentos? (sí/no) ")
                                                    if respuesta == "sí":
                                                        respuesta = hacer_pregunta("¿Se usa para cortar? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser un cuchillo, tijeras o pelador.")
                                                            return True
                                                        else:
                                                            respuesta = hacer_pregunta("¿Se usa para mezclar? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser una batidora, licuadora o espátula.")
                                                                return True
                                                            else:
                                                                print("Puede ser una sartén, olla o cacerola.")
                                                                return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Se usa para comer? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser un plato, vaso o cubiertos.")
                                                            return True
                                                        else:
                                                            print("Puede ser una bandeja o jarra.")
                                                            return True
                                                else:
                                                    respuesta = hacer_pregunta("¿Se usa para la limpieza? (sí/no) ")
                                                    if respuesta == "sí":
                                                        respuesta = hacer_pregunta("¿Se usa para barrer? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser una escoba o recogedor.")
                                                            return True
                                                        else:
                                                            respuesta = hacer_pregunta("¿Se usa para lavar? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser una esponja o cepillo.")
                                                                return True
                                                            else:
                                                                print("Puede ser un trapeador o una toalla.")
                                                                return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Se usa en la higiene personal?")
                                                    if respuesta == "sí":
                                                        print ("Puede ser un cepillo de dientes, crema, pasta, jabón, perfume o desodorante")
                                                        return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Se usa en la oficina o para estudiar? (sí/no) ")
                                                        if respuesta == "sí":
                                                            respuesta = hacer_pregunta("¿Se usa para escribir? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser un lápiz, bolígrafo o marcador.")
                                                                return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Se usa para medir? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser una regla o transportador.")
                                                                    return True
                                                                else:
                                                                    print("Puede ser un clip o una grapadora.")
                                                                    return True
                                                        else:
                                                            respuesta = hacer_pregunta("¿Se usa en el hogar? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser un destapador, sacacorchos o tijeras.")
                                                                return True
                                                            else:
                                                                print("Puede ser un martillo, alicate o destornillador.")
                                                                return True
                                            else:
                                                respuesta = hacer_pregunta("¿Es una fuente de energía? (sí/no) ")
                                                if respuesta == "sí":
                                                    respuesta = hacer_pregunta("¿Es una fuente de energía renovable? (sí/no) ")
                                                    if respuesta == "sí":
                                                        respuesta = hacer_pregunta("¿Proviene del sol? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser energía solar fotovoltaica o solar térmica.")
                                                            return True
                                                        else:
                                                            respuesta = hacer_pregunta("¿Proviene del viento? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser energía eólica.")
                                                                return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Proviene del agua? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    respuesta = hacer_pregunta("¿Proviene de ríos? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Puede ser energía hidroeléctrica.")
                                                                        return True
                                                                    else:
                                                                        print("Puede ser energía mareomotriz o undimotriz.")
                                                                        return True
                                                                else:
                                                                    print("Puede ser biomasa o biogás.")
                                                                    return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Proviene de combustibles fósiles? (sí/no) ")
                                                        if respuesta == "sí":
                                                            respuesta = hacer_pregunta("¿Proviene del carbón? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser energía derivada del carbón.")
                                                                return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Proviene del petróleo? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser energía derivada del petróleo, como gasolina o diésel.")
                                                                    return True
                                                                else:
                                                                    print("Puede ser energía derivada del gas natural.")
                                                                    return True
                                                        else:
                                                            print("Puede ser energía nuclear proveniente de la fisión de uranio o plutonio.")
                                                            return True
                                                else:
                                                    respuesta = hacer_pregunta("¿Es un lugar? (sí/no) ")
                                                    if respuesta == "sí":
                                                        respuesta = hacer_pregunta("¿Es un lugar natural? (sí/no) ")
                                                        if respuesta == "sí":
                                                            respuesta = hacer_pregunta("¿Es un ecosistema? (sí/no) ")
                                                            if respuesta == "sí":
                                                                respuesta = hacer_pregunta("¿Es terrestre? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser un bosque, selva, desierto, tundra o pradera.")
                                                                    return True
                                                                else:
                                                                    print("Puede ser un océano, río, lago, manglar o arrecife de coral.")
                                                                    return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Es una montaña? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser una montaña, volcán o meseta.")
                                                                    return True
                                                                else:
                                                                    respuesta = hacer_pregunta("¿Es una cueva? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Puede ser una cueva o una gruta.")
                                                                        return True
                                                                    else:
                                                                        print("Puede ser un lago, río, cascada o glaciar.")
                                                                        return True
                                                        else:
                                                            respuesta = hacer_pregunta("¿Es un lugar urbano? (sí/no) ")
                                                            if respuesta == "sí":
                                                                respuesta = hacer_pregunta("¿Es un lugar público? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    respuesta = hacer_pregunta("¿Es un edificio? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Puede ser un hospital, escuela, biblioteca, museo o estación de transporte.")
                                                                        return True
                                                                    else:
                                                                        print("Puede ser un parque, plaza, aeropuerto estadio.")
                                                                        return True
                                                                else:
                                                                    respuesta = hacer_pregunta("¿Es para fines comerciales? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Puede ser una tienda")
                                                                        return True
                                                                    print("Puede ser una casa, departamento o residencia privada.")
                                                                    return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Es un área de cultivo? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser una granja, plantación o rancho.")
                                                                    return True
                                                                else:
                                                                    print("Puede ser un parque nacional o una reserva ecológica.")
                                                                    return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Es un medio de comunicación? (sí/no) ")
                                                        if respuesta == "sí":
                                                            respuesta = hacer_pregunta("¿Es un medio de comunicación masivo? (sí/no) ")
                                                            if respuesta == "sí":
                                                                respuesta = hacer_pregunta("¿Es un medio impreso? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Es un periódico, revista o libro.")
                                                                    return True
                                                                else:
                                                                    respuesta = hacer_pregunta("¿Es un medio audiovisual? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Es la radio, televisión o cine.")
                                                                        return True
                                                                    else:
                                                                        print("Es internet o redes sociales.")
                                                                        return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Es un medio de comunicación interpersonal? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    respuesta = hacer_pregunta("¿Es oral? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Es una conversación o una llamada telefónica.")
                                                                        return True
                                                                    else:
                                                                        respuesta = hacer_pregunta("¿Es escrito? (sí/no) ")
                                                                        if respuesta == "sí":
                                                                            print("Es una carta, un mensaje de texto o un correo electrónico.")
                                                                            return True
                                                                        else:
                                                                            print("Es un gesto o una señal no verbal.")
                                                                            return True
                                                        else:
                                                            respuesta = hacer_pregunta("¿Es un medio artístico de comunicación? (sí/no) ")
                                                            if respuesta == "sí":
                                                                respuesta = hacer_pregunta("¿Es visual? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    respuesta = hacer_pregunta("¿Es una pintura o escultura? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Es una obra plástica como una pintura o escultura.")
                                                                        return True
                                                                    else:
                                                                        respuesta = hacer_pregunta("¿Es una fotografía o cine? (sí/no) ")
                                                                        if respuesta == "sí":
                                                                            print("Es una fotografía o una película cinematográfica.")
                                                                            return True
                                                                        else:
                                                                            print("Es otra forma de arte visual como una ilustración o diseño gráfico.")
                                                                            return True
                                                                else:
                                                                    respuesta = hacer_pregunta("¿Es escénico? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        respuesta = hacer_pregunta("¿Es teatro o danza? (teatro/danza) ")
                                                                        if respuesta == "teatro":
                                                                            print("Es una obra de teatro.")
                                                                            return True
                                                                        else:
                                                                            print("Es una obra de danza.")
                                                                            return True
                                                                    else:
                                                                        respuesta = hacer_pregunta("¿Es musical? (sí/no) ")
                                                                        if respuesta == "sí":
                                                                            respuesta = hacer_pregunta("¿Es instrumental o vocal? (instrumental/vocal) ")
                                                                            if respuesta == "instrumental":
                                                                                print("Es una obra musical instrumental.")
                                                                                return True
                                                                            else:
                                                                                print("Es una canción o una ópera.")
                                                                                return True
                                                                        else:
                                                                            print("Es una forma de arte conceptual o experimental.")
                                                                            return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Es una señalización? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    respuesta = hacer_pregunta("¿Es una señal de tránsito? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        respuesta = hacer_pregunta("¿Es una señal preventiva? (sí/no) ")
                                                                        if respuesta == "sí":
                                                                            print("Es una señal de precaución, como curva peligrosa o cruce de peatones.")
                                                                            return True
                                                                        else:
                                                                            respuesta = hacer_pregunta("¿Es una señal restrictiva? (sí/no) ")
                                                                            if respuesta == "sí":
                                                                                print("Es una señal de límite de velocidad o prohibición.")
                                                                                return True
                                                                            else:
                                                                                print("Es una señal informativa, como nombres de calles o servicios.")
                                                                                return True
                                                                    else:
                                                                        respuesta = hacer_pregunta("¿Es una señal de seguridad? (sí/no) ")
                                                                        if respuesta == "sí":
                                                                            respuesta = hacer_pregunta("¿Es una señal de emergencia? (sí/no) ")
                                                                            if respuesta == "sí":
                                                                                print("Es una salida de emergencia o punto de reunión.")
                                                                                return True
                                                                            else:
                                                                                print("Es una señal de advertencia de peligro, como material inflamable.")
                                                                                return True
                                                                        else:
                                                                            print("Es otro tipo de señal, como indicaciones en aeropuertos o estaciones de tren.")
                                                                            return True
    else:
        respuesta = hacer_pregunta("¿Es un sentimiento? (sí/no) ")
        if respuesta == "sí":
            respuesta = hacer_pregunta("¿Es un sentimiento positivo? (sí/no) ")
            if respuesta == "sí":
                respuesta = hacer_pregunta("¿Está relacionado con la felicidad? (sí/no) ")
                if respuesta == "sí":
                    respuesta = hacer_pregunta("¿Es alegría? (sí/no) ")
                    if respuesta == "sí":
                        print("Es felicidad, entusiasmo o gratitud.")
                        return True
                    else:
                        print("Es amor, cariño o afecto.")
                        return True
                else:
                    respuesta = hacer_pregunta("¿Está relacionado con la calma? (sí/no) ")
                    if respuesta == "sí":
                        print("Es paz, tranquilidad o alivio.")
                        return True
                    else:
                        print("Es esperanza o satisfacción.")
                        return True
            else:
                respuesta = hacer_pregunta("¿Es un sentimiento negativo? (sí/no) ")
                if respuesta == "sí":
                    respuesta = hacer_pregunta("¿Está relacionado con el miedo? (sí/no) ")
                    if respuesta == "sí":
                        print("Es temor, ansiedad o inseguridad.")
                        return True
                    else:
                        respuesta = hacer_pregunta("¿Está relacionado con la tristeza? (sí/no) ")
                        if respuesta == "sí":
                            print("Es melancolía, desilusión o nostalgia.")
                            return True
                        else:
                            respuesta = hacer_pregunta("¿Está relacionado con el enojo? (sí/no) ")
                            if respuesta == "sí":
                                print("Es ira, frustración o resentimiento.")
                                return True
                            else:
                                print("Es asco o desprecio.")
                                return True
                else:
                    print("Es una emoción compleja o ambigua, como sorpresa o nostalgia.")
                    return True
        else:
            respuesta = hacer_pregunta("¿Es una idea? (sí/no) ")
            if respuesta == "sí":
                respuesta = hacer_pregunta("¿Es una idea abstracta? (sí/no) ")
                if respuesta == "sí":
                    respuesta = hacer_pregunta("¿Está relacionada con la filosofía o la moral? (sí/no) ")
                    if respuesta == "sí":
                        print("Es un concepto filosófico como justicia, libertad o ética.")
                        return True
                    else:
                        respuesta = hacer_pregunta("¿Está relacionada con las matemáticas o la lógica? (sí/no) ")
                        if respuesta == "sí":
                            print("Es un concepto matemático o lógico, como infinito o causalidad.")
                            return True
                        else:
                            print("Es un concepto abstracto como belleza, verdad o tiempo.")
                            return True
                else:
                    respuesta = hacer_pregunta("¿Es una idea aplicada o práctica? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Es una idea relacionada con la ciencia o la tecnología? (sí/no) ")
                        if respuesta == "sí":
                            print("Es un concepto científico o tecnológico, como evolución o inteligencia artificial.")
                            return True
                        else:
                            respuesta = hacer_pregunta("¿Está relacionada con la creatividad o el arte? (sí/no) ")
                            if respuesta == "sí":
                                print("Es una idea artística o creativa, como un estilo de pintura o un movimiento literario.")
                                return True
                            else:
                                respuesta = hacer_pregunta("¿Está relacionada con la política o la sociedad? (sí/no) ")
                                if respuesta == "sí":
                                    print("Es un concepto político o social, como democracia o capitalismo.")
                                    return True
                                else:
                                    print("Es una idea práctica o estratégica, como un modelo de negocio o un plan de proyecto.")
                                    return True
            else:
                respuesta = hacer_pregunta("¿Es un valor? (sí/no) ")
                if respuesta == "sí":
                    respuesta = hacer_pregunta("¿Es un valor moral? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Está relacionado con el respeto hacia los demás? (sí/no) ")
                        if respuesta == "sí":
                            print("Es un valor como respeto, tolerancia o empatía.")
                            return True
                        else:
                            respuesta = hacer_pregunta("¿Implica actuar con honestidad y justicia? (sí/no) ")
                            if respuesta == "sí":
                                print("Es un valor como honestidad, justicia o integridad.")
                                return True
                            else:
                                print("Es un valor moral como responsabilidad o lealtad.")
                                return True
                    else:
                        respuesta = hacer_pregunta("¿Es un valor social? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Promueve la cooperación y convivencia? (sí/no) ")
                            if respuesta == "sí":
                                print("Es un valor social como solidaridad, cooperación o generosidad.")
                                return True
                            else:
                                print("Es un valor social como civismo o equidad.")
                                return True
                        else:
                            respuesta = hacer_pregunta("¿Es un valor personal? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Está relacionado con el esfuerzo y la superación? (sí/no) ")
                                if respuesta == "sí":
                                    print("Es un valor personal como disciplina, perseverancia o responsabilidad.")
                                    return True
                                else:
                                    print("Es un valor personal como autoestima o autonomía.")
                                    return True
                            else:
                                respuesta = hacer_pregunta("¿Es un valor cultural o empresarial? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Se enfoca en la innovación y la excelencia? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Es un valor empresarial como creatividad o excelencia.")
                                        return True
                                    else:
                                        print("Es un valor cultural o empresarial como identidad o compromiso.")
                                        return True
                                else:
                                    print("Es un valor general como libertad o gratitud.")
                                    return True
                else:
                    respuesta = hacer_pregunta("¿Es algo ficticio? (sí/no) ")
                    if respuesta == "sí":
                        respuesta = hacer_pregunta("¿Es un personaje? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es sobrenatural? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es mitológico? (sí/no) ")
                                if respuesta == "sí":
                                    print("Pueden ser monstruos, fantasmas o espíritus")
                                    return True
                                else:
                                    print("Pueden ser criaturas míticas, dioses o seres divinos.")
                                    return True
                            else:
                                print("Es un personaje ficticio de cine, libros o videojuegos.")
                            return True
                        else:
                            respuesta = hacer_pregunta("¿Es un lugar? (sí/no) ")
                            if respuesta == "sí":
                                print("Es una ciudad de fantasía o realidad alterna.")
                                return True
                            else:
                                print("Es un concepto ficticio como una historia, cuento o un recuerdo")
                                return True
                    else:
                        respuesta = hacer_pregunta("¿Es algo histórico? (sí/no) ")
                        if respuesta == "sí":
                            respuesta = hacer_pregunta("¿Es un personaje? (sí/no) ")
                            if respuesta == "sí":
                                print("Puede ser un personaje histórico")
                                return True
                            else:
                                respuesta = hacer_pregunta("¿Es un hecho? (sí/no) ")
                                if respuesta == "sí":
                                    print("Puede ser un momento histórico como la segunda guerra mundial o la revolución")
                                    return True
                                else:
                                    print("Puede ser un lugar histórico.")
                                    return True
                        else:
                            respuesta = hacer_pregunta("¿Es una festividad? (sí/no) ")
                            if respuesta == "sí":
                                respuesta = hacer_pregunta("¿Es de origen religioso? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Es una festividad cristiana? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser Navidad, Semana Santa o Día de Reyes.")
                                        return True
                                    else:
                                        respuesta = hacer_pregunta("¿Es una festividad de otra religión? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser Hanukkah, Ramadán o Diwali.")
                                            return True
                                else:
                                    respuesta = hacer_pregunta("¿Es una festividad nacional o patriótica? (sí/no) ")
                                    if respuesta == "sí":
                                        print("Puede ser el Día de la Independencia, Revolución o Constitución.")
                                        return True
                                    else:
                                        respuesta = hacer_pregunta("¿Es una festividad cultural o tradicional? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser el Día de Muertos, Carnaval o Año Nuevo Chino.")
                                            return True
                                        else:
                                            respuesta = hacer_pregunta("¿Es una festividad internacional? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser el Día del Trabajo, Halloween o Año Nuevo.")
                                                return True
                                            else:
                                                print("Es otro tipo de festividad.")
                                                return True
                            else:
                                respuesta = hacer_pregunta("¿Es una acción? (sí/no) ")
                                if respuesta == "sí":
                                    respuesta = hacer_pregunta("¿Implica movimiento físico? (sí/no) ")
                                    if respuesta == "sí":
                                        respuesta = hacer_pregunta("¿Es una acción cotidiana? (sí/no) ")
                                        if respuesta == "sí":
                                            print("Puede ser caminar, correr, comer o dormir.")
                                            return True
                                        else:
                                            respuesta = hacer_pregunta("¿Es una acción deportiva? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser nadar, saltar, lanzar o patear.")
                                                return True
                                            else:
                                                respuesta = hacer_pregunta("¿Es una acción laboral o técnica? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser soldar, ensamblar, programar o construir.")
                                                    return True
                                                else:
                                                    print("Es otro tipo de acción física.")
                                                    return True
                                    else:
                                        respuesta = hacer_pregunta("¿Implica un proceso mental o emocional? (sí/no) ")
                                        if respuesta == "sí":
                                            respuesta = hacer_pregunta("¿Es una acción cognitiva? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser pensar, recordar, analizar o imaginar.")
                                                return True
                                            else:
                                                respuesta = hacer_pregunta("¿Es una acción emocional? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser amar, odiar, temer o alegrarse.")
                                                    return True
                                                else:
                                                    print("Es otro tipo de acción mental o emocional.")
                                                    return True
                                        else:
                                            print("Es otro tipo de acción.")
                                else:
                                    respuesta = hacer_pregunta("¿Es un concepto que cuantifica algo? (sí/no) ")
                                    if respuesta == "sí":
                                        respuesta = hacer_pregunta("¿Mide tiempo? (sí/no) ")
                                        if respuesta == "sí":
                                            respuesta = hacer_pregunta("¿Es una unidad de tiempo? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser segundo, minuto, hora, día, mes o año.")
                                                return True
                                            else:
                                                print("Puede ser un concepto relacionado con el tiempo, como duración o antigüedad.")
                                                return True
                                        else:
                                            respuesta = hacer_pregunta("¿Mide distancia o longitud? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser metro, kilómetro, milla, centímetro o pulgada.")
                                                return True
                                            else:
                                                respuesta = hacer_pregunta("¿Mide peso o masa? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser gramo, kilogramo, tonelada o libra.")
                                                    return True
                                                else:
                                                    respuesta = hacer_pregunta("¿Mide volumen o capacidad? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser litro, mililitro, metro cúbico o galón.")
                                                        return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Mide temperatura? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser grado Celsius, Fahrenheit o Kelvin.")
                                                            return True
                                                        else:
                                                            respuesta = hacer_pregunta("¿Mide dinero o valor económico? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser peso, dólar, euro o yen.")
                                                                return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Mide velocidad? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser kilómetros por hora, metros por segundo o nudos.")
                                                                    return True
                                                                else:
                                                                    respuesta = hacer_pregunta("¿Mide fuerza o energía? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Puede ser joule, newton o vatio.")
                                                                        return True
                                                                    else:
                                                                        respuesta = hacer_pregunta("¿Mide cantidad en términos generales? (sí/no) ")
                                                                        if respuesta == "sí":
                                                                            print("Puede ser docena, centenar, millar o mol.")
                                                                            return True
                                                                        else:
                                                                            print("Es otro tipo de concepto cuantificable.")
                                                                            return True
                                    else:
                                        respuesta = hacer_pregunta("¿Es un concepto que explica algo? (sí/no) ")
                                        if respuesta == "sí":
                                            respuesta = hacer_pregunta("¿Es un principio o ley científica? (sí/no) ")
                                            if respuesta == "sí":
                                                print("Puede ser la ley de la gravedad, la teoría de la relatividad o la ley de la termodinámica.")
                                                return True
                                            else:
                                                respuesta = hacer_pregunta("¿Es una norma o ley jurídica? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser una ley constitucional, un reglamento o un tratado internacional.")
                                                    return True
                                                else:
                                                    respuesta = hacer_pregunta("¿Es una teoría o modelo explicativo? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser el modelo atómico, la teoría del Big Bang o la teoría del aprendizaje.")
                                                        return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Es un concepto filosófico o abstracto? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser el libre albedrío, la justicia o la existencia.")
                                                            return True
                                                        else:
                                                            respuesta = hacer_pregunta("¿Es un método o procedimiento? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser el método científico, el análisis SWOT o el método inductivo.")
                                                                return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Es una hipótesis o suposición? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser una hipótesis científica, una conjetura matemática o una inferencia lógica.")
                                                                    return True
                                                                else:
                                                                    print("Es otro tipo de concepto explicativo.")
                                                                    return True
                                        else:
                                            respuesta = hacer_pregunta("¿Es un fenómeno social o cultural? (sí/no) ")
                                            if respuesta == "sí":
                                                respuesta = hacer_pregunta("¿Es un movimiento social? (sí/no) ")
                                                if respuesta == "sí":
                                                    print("Puede ser el feminismo, el ambientalismo o el movimiento obrero.")
                                                    return True
                                                else:
                                                    respuesta = hacer_pregunta("¿Es una tendencia o cambio cultural? (sí/no) ")
                                                    if respuesta == "sí":
                                                        print("Puede ser la globalización, la digitalización o la evolución del lenguaje.")
                                                        return True
                                                    else:
                                                        respuesta = hacer_pregunta("¿Es una práctica o costumbre social? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser la hospitalidad, el saludo con la mano o las festividades tradicionales.")
                                                            return True
                                                        else:
                                                            respuesta = hacer_pregunta("¿Es un conflicto o problema social? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser la pobreza, la desigualdad o la discriminación.")
                                                                return True
                                                            else:
                                                                respuesta = hacer_pregunta("¿Es una estructura o institución social? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser la familia, el gobierno o el sistema educativo.")
                                                                    return True
                                                                else:
                                                                    respuesta = hacer_pregunta("¿Es un fenómeno económico? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Puede ser la inflación, la recesión o el desempleo.")
                                                                        return True
                                                                    else:
                                                                        print("Es otro tipo de fenómeno social o cultural.")
                                                                        return True
                                            else:
                                                respuesta = hacer_pregunta("¿Es un dato digital? (sí/no) ")
                                                if respuesta == "sí":
                                                    respuesta = hacer_pregunta("¿Es un archivo? (sí/no) ")
                                                    if respuesta == "sí":
                                                        respuesta = hacer_pregunta("¿Es un archivo de texto? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser un documento de Word, un PDF o un archivo TXT.")
                                                        else:
                                                            respuesta = hacer_pregunta("¿Es un archivo multimedia? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser una imagen, un video o un archivo de audio.")
                                                            else:
                                                                respuesta = hacer_pregunta("¿Es un archivo de datos estructurados? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser un archivo CSV, JSON o XML.")
                                                                else:
                                                                    print("Puede ser otro tipo de archivo como un ejecutable o comprimido.")
                                                    else:
                                                        respuesta = hacer_pregunta("¿Es un conjunto de datos? (sí/no) ")
                                                        if respuesta == "sí":
                                                            print("Puede ser una base de datos, un dataset de aprendizaje automático o un registro de logs.")
                                                        else:
                                                            respuesta = hacer_pregunta("¿Es una credencial digital? (sí/no) ")
                                                            if respuesta == "sí":
                                                                print("Puede ser una contraseña, una firma digital o un token de autenticación.")
                                                            else:
                                                                respuesta = hacer_pregunta("¿Es una transacción digital? (sí/no) ")
                                                                if respuesta == "sí":
                                                                    print("Puede ser una compra en línea, una transferencia bancaria o una transacción con criptomonedas.")
                                                                else:
                                                                    respuesta = hacer_pregunta("¿Es un identificador digital? (sí/no) ")
                                                                    if respuesta == "sí":
                                                                        print("Puede ser una dirección IP, un nombre de usuario o una dirección de correo electrónico.")
                                                                    else:
                                                                        print("Es otro tipo de dato digital.")


    print("\n😔 No pude adivinar en lo que estabas pensando.")
    return False

def main():
    """Función principal del juego"""
    while True:
        jugar_una_partida()
        
        respuesta = validar_respuesta("\n¿Quieres jugar otra vez? (sí/no) ", 0)
        if respuesta == "no":
            print("\n¡Gracias por jugar! 👋 ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
