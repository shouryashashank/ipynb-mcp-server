import nbformat
from jupyter_client import KernelManager
from jupyter_client import NotebookClient
from jupyter_client import KernelClient
from jupyter_client import AsyncKernelManager
from jupyter_client import AsyncKernelClient
class PythonNotebook:
    def __init__(self):
        self.nb = nbformat.v4.new_notebook()

    async def initialize(self):
        self.nb_client = NotebookClient(self.nb)
        if self.nb_client.kc is None or not await self.nb_client.kc.is_alive():
            self.nb_client.create_kernel_manager()
            self.nb_client.start_new_kernel()
            self.nb_client.start_new_kernel_client()


    def add_code_cell(self, code):
        self.nb.cells.append(nbformat.v4.new_code_cell(code))
        # Return the index of the cell
        return len(self.nb.cells) - 1

    def execute(self):
        
        self.nb_client.execute()
        return self.nb

    def execute_cell(self, cell_index):
        
        self.nb_client.execute_cell(self.nb.cells[cell_index], cell_index)
        return self.nb.cells[cell_index]

    def save(self, file_path):
        with open(file_path, "w") as f:
            nbformat.write(self.nb, f)