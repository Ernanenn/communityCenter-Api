import requests
import pytest
import uuid

# --- Configuração Base ---
# URL base da API e a chave de acesso.
# **CORREÇÃO APLICADA AQUI**
BASE_URL = "https://cj98hakmf0.execute-api.us-east-1.amazonaws.com/phoebus-apps"
API_KEY = "d0efb067-f553-4c33-97ed-f532dd0d1db4"
HEADERS = {"apiKey": API_KEY, "Content-Type": "application/json"}


class TestCommunityCenterLifecycle:
    """
    Agrupa os testes que validam o ciclo de vida completo de um centro comunitário,
    garantindo a ordem correta de execução (Criar -> Atualizar -> Remover).
    """
    center_id = None  # Variável de classe para partilhar o ID entre os testes

    def test_1_create_new_center(self):
        """
        Passo 1: Cria um novo centro comunitário e guarda o seu ID.
        """
        print("\n[PASSO 1] Criando um novo centro...")
        # Usar um UUID para garantir que o nome do centro é sempre único
        unique_name = f"Centro de Teste de Ciclo de Vida - {uuid.uuid4()}"
        payload = {
            "name": unique_name,
            "address": "Rua do Ciclo de Vida, 789",
            "maxNumberOfPeople": 150,
            "currentNumberOfPeople": 50,
            "resources": {"doctor": 2, "volunteer": 8}
        }

        response = requests.post(f"{BASE_URL}/communityCenter", json=payload, headers=HEADERS)

        # Validação 1: A criação deve retornar status 201
        assert response.status_code == 201, f"Esperado status 201, mas foi obtido {response.status_code}"

        response_data = response.json()
        
        # Validação 2: A resposta deve conter o ID
        assert "communityCenterId" in response_data, "A resposta de criação não contém 'communityCenterId'"

        # Guarda o ID na variável da classe para o próximo teste
        self.__class__.center_id = response_data["communityCenterId"]
        print(f"[PASSO 1] Centro criado com sucesso. ID: {self.center_id}")
        assert self.center_id is not None

    def test_2_update_number_of_people(self):
        """
        Passo 2: Atualiza o número de pessoas do centro criado no passo anterior.
        """
        # Garante que o teste de criação foi executado antes e o ID foi guardado
        assert self.center_id is not None, "O ID do centro não foi guardado; o teste de criação pode ter falhado."
        
        print(f"\n[PASSO 2] Atualizando o número de pessoas do centro ID: {self.center_id}...")
        new_number_of_people = 125
        update_payload = {"currentNumberOfPeople": new_number_of_people}

        response = requests.put(
            f"{BASE_URL}/communityCenter/{self.center_id}/currentNumberOfPeople",
            json=update_payload,
            headers=HEADERS
        )

        # Validação: A atualização deve retornar status 204
        assert response.status_code == 204, f"Esperado status 204, mas foi obtido {response.status_code}"
        print("[PASSO 2] Atualização bem-sucedida.")

    def test_3_remove_center(self):
        """
        Passo 3: Remove o centro e verifica se ele foi realmente apagado.
        """
        # Garante que o ID do centro está disponível
        assert self.center_id is not None, "O ID do centro não foi guardado; o teste de criação pode ter falhado."

        print(f"\n[PASSO 3] Removendo o centro ID: {self.center_id}...")
        
        delete_response = requests.delete(f"{BASE_URL}/communityCenter/{self.center_id}", headers=HEADERS)

        # Validação 1: A remoção deve retornar status 204
        assert delete_response.status_code == 204, f"Esperado status 204, mas foi obtido {delete_response.status_code}"
        print("[PASSO 3] Remoção bem-sucedida.")
        
        # Validação Extra: Tenta obter o centro removido para garantir que não existe mais
        print(f"[PASSO 3 - Verificação] Tentando obter o centro removido ID: {self.center_id}...")
        get_response = requests.get(f"{BASE_URL}/communityCenter/{self.center_id}", headers=HEADERS)
        
        # Validação 2: A API retorna 403 (Forbidden) para um centro que não existe ou não está acessível.
        assert get_response.status_code == 403, f"Esperado status 403, mas foi obtido {get_response.status_code}. O centro pode não ter sido removido."
        print("[PASSO 3 - Verificação] Confirmação de que o centro foi removido com sucesso.")