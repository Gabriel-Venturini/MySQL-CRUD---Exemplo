import unittest
from app.connect import connect
from app.operations import create

class TestConnect(unittest.TestCase):
    # you can test all operations here

    def test_create(self):
        # test if the function can insert data into the db
        connection = connect('maia1904')
        # dataset to test the function
        data = [['Carlos Almeida', 'carlos.almeida@example.com', 'Backend Developer', 2500.00],
                ['Julia Nogueira', 'julia.nogueira@example.com', 'Frontend Developer', 3000.00],
                ['Renato Souza', 'renato.souza@example.com', 'Data Analyst', 2800.00],
                ['Beatriz Lima', 'beatriz.lima@example.com', 'Project Manager', 4500.00],
                ['Eduardo Pereira', 'eduardo.pereira@example.com', 'UX Designer', 3200.00]]
        
        # for loop to insert the values
        for record in data:
            nome, email, cargo, salario = record  # unpack values
            result = create(connection, nome, email, cargo, salario)  # calls the function
            self.assertEqual(result, "Data inserted with success.", result) # tests it


if __name__ == '__main__':
    unittest.main()