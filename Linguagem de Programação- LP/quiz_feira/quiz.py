import streamlit as st


#banco de perguntas
perguntas = [
    # perguntas 6 ano
    {           
        "pergunta": "Qual nome a Escola Estadual Liberato de Castro teve originalmente?",
        "opcoes": ["Escola Estadual Liberato de Castro", "Ginásio São Tomás de Aquino", "Ginásio Cícero de Castro", "Escola Estadual Cícero de Castro"],
        "resposta": "Ginásio São Tomás de Aquino"
    },
    {
        "pergunta": "Qual das alternativas a seguir é considerada um patrimônio/bem tombado de Marliéria?",
        "opcoes": ["Escola Estadual Liberato de Castro", "Posto de Saúde", "Capela Velório", "Mercearia Nossa Gente Irmãos Borges"],
        "resposta": "Escola Estadual Liberato de Castro"
    },
    {
        "pergunta": "Em que ano a escola passou a se chamar Liberato de Castro ,tendo sido fundada originalmente com o nome diferente ?",
        "opcoes": ["1965", "1966", "1967", "1968"],
        "resposta": "1968"
    },
    # perguntas 7 ano
    {             
        "pergunta": "Qual foi o primeiro aluno a ganhar medalha na OBMEP na EELC?",
        "opcoes": ["Denian Castro", "Sandy Verissimo", "Pamela Castro", "Luisa Viana"],
        "resposta": "Denian Castro"
    },
    {
        "pergunta": "Qual foi o ano da primeira edição da OBMEP?",
        "opcoes": ["2003", "2004", "2005", "2006"],
        "resposta": "2005"
    },
    {
        "pergunta": "Quem foi a primeira Professora da Sala de Recursos?",
        "opcoes": ["Joelma Batista", "Elisângela Malaquias", "Kerley Araújo", "Ariadne Paiva"],
        "resposta": "Elisângela Malaquias"
    },
    # perguntas 8 ano
    {
        "pergunta": "Quem assumiu a direção da escola em 1965 como seu primeiro diretor?",
        "opcoes": ["Cícero de Castro", "Lelia De Castro Quintão ", "Otacilio Fernandes D'avila", "Ariadne Paiva Araújo"],
        "resposta": "Otacilio Fernandes D'avila"
    },
    {
        "pergunta": "Quem assumiu o cargo de diretor da escola no ano de 2005?",
        "opcoes": ["Celia de Barros Moreira", "Rosane de Assis Horta", "Vera Maria Dos Santos ", "Ariadne Paiva Araújo"],
        "resposta": "Ariadne Paiva Araújo"
    },
    {
        "pergunta": "Qual professor atualmente leciona na EELC?",
        "opcoes": ["Hamilton Moreira Quintão", "Elaine Maia Lana", "Rosane Assis Horta","Elisângela Malaquias Quintão"],
        "resposta": "Elisângela Malaquias Quintão"\
    },
    # perguntas 9 ano
    {
        "pergunta": "Quantos alunos havia na primeira turma de formandos em 1965?",
        "opcoes": ["20", "21", "22", "23"],
        "resposta": "23"
    },
    {
        "pergunta": "Quem trabalhou como uma das primeiras cantineiras da escola, preparando a merenda dos alunos?",
        "opcoes": ["Marta de Castro Pereira", "Teresinha de Jesus ", "Maria Carmo Pinto", "Darci Dias Reis"],
        "resposta": "Teresinha de Jesus"
    },
    # perguntas 1 ano
    {
        "pergunta": "Quem foi o doador do terreno para a construção do ginásio e colégio normal, intitulado hoje como EELC?",
        "opcoes": ["Antônio Félix de Castro", "Félix Quintão Castro", "Félix de Castro", "Félix de Castro Quintão"],
        "resposta": "Félix de Castro"
    },
    {
        "pergunta": "Em que mês e ano reuniram a primeira turma para as primeiras aulas na sacristia da Igreja Matriz?",
        "opcoes": ["Janeiro de 1961", "Outubro de 1961", "Dezembro de 1961", "Agosto de 1961"],
        "resposta": "Dezembro de 1961"
    },
    {
        "pergunta": "Qual instituição religiosa teve papel central na vida comunitária de Marliéria?",
        "opcoes": ["Capela Santo Antônio", "Paróquia Nossa Senhora das Dores", "Paróquia São José", "Catedral de Belo Horizonte"],
        "resposta": "Paróquia Nossa Senhora das Dores"\
    },
    #perguntas 2 ano
    {
        "pergunta": "Onde muitas festas e formaturas aconteciam em Marliéria?",
        "opcoes": ["No teatro", "Na Igreja Matriz", "Na praça de esportes", "Na prefeitura"],
        "resposta": "Na Igreja Matriz"
    },
    {
        "pergunta": "Quais eram as referências ou bases utilizadas pelos alunos para criar e organizar as antigas feiras culturais?",
        "opcoes": ["Eles pesquisavam apenas em sites da internet", "Eles se baseavam em livros, revistas, jornais e relatos orais", "Usavam somente filmes e novelas da televisão", "Seguiam apenas conversas informais com amigos"],
        "resposta": "Eles se baseavam em livros revistas, jornais e relatos orais"
    },
    {
        "pergunta": "Quais festivais eram organizados para revelar talentos locais e abordar lendas e costumes?",
        "opcoes": ["Festival de Esportes  e Festival de Ciências", "Festival de Folclore e Festival de Canção", "Festival de Teatro e Festival de Dança", "Festival de História e Festival de Matemática"],
        "resposta": "Festival de Folclore e Festival de Canção"\
    },
    #perguntas 3 ano
    {
        "pergunta": "Durante a ditadura militar no Brasil, qual foi a postura do Padre Cícero que o tornou alvo de vigilância e perseguição pelos militares?",
        "opcoes": ["Sua aproximação com  grupos políticos de oposição armada ao regime", "O apoio às prostitutas, oferecendo conforto espiritual, cuidados de saúde e sustento", "Sua atuação em defesa da educação da justiça social e dos direitos humanos, criando desigualdades", "A criação de um movimento estudantil contra a ditadura dentro da Igreja"],
        "resposta": "Sua atuação em defesa da educação da justiça social e dos direitos humanos, criando desigualdades."
    },
    {
        "pergunta": "Quando a biblioteca Padre Cícero de Castro foi criada?",
        "opcoes": ["Fevereiro de 1990", "Junho de 1987", "Junho de 1985", "Julho de 1987"],
        "resposta": "Junho de 1987"
    },
    {
        "pergunta": "Qual é o município que possui uma escola em homenagem a Padre Cícero?",
        "opcoes": ["Coronel Fabriciano", "Timóteo", "Marliéria", "Ipatinga"],
        "resposta": "Ipatinga"\
        
    }
]

# Estado da sessão para progresso
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.acertos = 0

st.title("🎓 Quiz Feira Cultural - EELC 60 anos")
# dentro do st.write colocar uma introducao sobre o quiz, quais assuntos estao abordados e que o resultado sera mostrado no final.
st.write("Prepara-se para testar seus conhecimentos sobre a história da Escola Estadual Liberato de Castro (EELC) e do munícipio de Marliéria-MG. Mostre o quanto você sabe e descubra curiosidades incríveis enquanto celebramos juntos os 60 anos da nossa escola!")

# Exibir apenas a pergunta atual
if st.session_state.indice < len(perguntas):
    q = perguntas[st.session_state.indice]
    
    st.subheader(f"Pergunta {st.session_state.indice + 1}:")
    st.write(q["pergunta"])

    escolha = st.radio("Escolha uma alternativa:", q["opcoes"], key=st.session_state.indice)

    if st.button("Responder"):
        if escolha == q["resposta"]:
            st.success("✅ Resposta correta!")
            st.session_state.acertos += 1
        else:
            st.error(f"❌ Resposta errada! A correta era: {q['resposta']}")
        
        st.session_state.indice += 1
        st.rerun()

else:
    st.success(f"Fim do Quiz! Você acertou {st.session_state.acertos / len(perguntas)*100}% de {len(perguntas)} perguntas. 🎉")
    if st.button("Reiniciar"):
        st.session_state.indice = 0
        st.session_state.acertos = 0
        st.rerun()
