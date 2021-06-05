import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class View(tk.Tk):
    """docstring for View."""

    PAD = 10

    def __init__(self, controller):
        super(View, self).__init__()
        self.controller = controller
        self.title('Georg Stage vagtplanlægger')
        self.value_var = tk.StringVar()
        self._make_menu()
        self._make_main_frame()
        self._make_entries()
        self._make_buttons()


    def main(self):
        print('In main of view ')
        self.mainloop()

    def _make_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)
        fileMenu = tk.Menu(menu)
        menu.add_cascade(label="Filer", menu=fileMenu)
        functionMenu = tk.Menu(menu)
        menu.add_cascade(label="Funktioner", menu=functionMenu)
        fileMenu.add_command(label="Åben", command=self._on_open)
        fileMenu.add_command(label="Gem som", command=self._on_save_as)
        functionMenu.add_command(label="Udfyld resten", command=self.controller.fill_day)

    def _on_open(self):
        filename = filedialog.askopenfilename()
        self.controller.open_file(filename)

    def _on_save_as(self):
        filename = filedialog.asksaveasfilename()
        self.controller.save_file(filename)


    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_entries(self):
        ent = ttk.Entry(
            self.main_frm,
            justify='right',
            textvariable=self.value_var,
            state='disabled')
        ent.pack()

    def _make_buttons(self):
        btn = ttk.Button(self.main_frm, text='INCR', command=self.controller.on_incr)
        btn.pack(side='left')