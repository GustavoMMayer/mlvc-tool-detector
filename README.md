# ToolDetector API - Visão Computacional

Sistema de detecção de objetos focado no reconhecimento automático de ferramentas manuais e elétricas via API RESTful.

## 🔗 Links Principais
- **Quadro Trello (Público):** [Inserir Link do Trello Aqui]
- **Vídeo de Demonstração:** [Inserir Link do Vídeo (Drive/YouTube) Aqui]

## 🛠️ Dataset
O dataset é composto por 10 classes de ferramentas:
1. Alicate (`pliers`)
2. Martelo (`hammer`)
3. Chave de fenda (`screwdriver`)
4. Chave inglesa (`wrench`)
5. Serrote (`saw`)
6. Trena (`tape_measure`)
7. Furadeira (`drill`)
8. Nível (`level`)
9. Estilete (`cutter`)
10. Chave Allen (`hex_key`)

## 🚀 Como Executar

### 1. Clonar e Instalar Dependências
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt