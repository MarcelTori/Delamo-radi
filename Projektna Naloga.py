import tkinter as tk

EMPTY = 0


class Igra:
    def __init__(self):
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
        self.move = 'X'
        self.previous = 'O'
        self.is_a_draw = False
        self.zmagovalec = None

    def poteza(self, x, y):
        if self.board[y][x] == EMPTY:
            self.board[y][x] = self.move
            if self.move == 'X':
                self.move = 'O'
                self.previous = 'X'
                return True
            else:
                self.move = 'X'
                self.previous = 'O'
                return True
        return False

    def winner(self):
        for y in range(3):
            if self.board[y] == [self.previous, self.previous, self.previous]:
                return True

        for x in range(3):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] == self.previous:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.previous:
            return True

        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.previous:
            return True
        
        if self.draw():
            self.is_a_draw = True
            return True
        else:
            return False

    def draw(self):
        for vrstica in self.board:
            for i in vrstica:
                if i == EMPTY:
                    return False
        return True

class Vmesnik:
    def __init__(self, okno):
        self.igra = Igra()
        self.obvestilo = tk.Label(okno, text='TIC TAC TOE')
        self.obvestilo.grid(row=0, column=0)
        

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []
        for vrstica in range(3):
            vrstica_gumbov = []
            for stolpec in range(3):
                def pritisni_gumb(vrstica=vrstica, stolpec=stolpec):
                    self.pritisni(vrstica, stolpec)
                gumb = tk.Button(prikaz_plosce, text='', height=5, width=10, command=pritisni_gumb)
                gumb.grid(row=vrstica, column=stolpec)
                vrstica_gumbov.append(gumb)
            self.gumbi.append(vrstica_gumbov)
        prikaz_plosce.grid(row=1, column=0, columnspan=2)

    def pritisni(self, vrstica, stolpec):
        if self.igra.poteza(vrstica, stolpec):
            self.gumbi[vrstica][stolpec].config(text = self.igra.move)
            if self.igra.winner() and not self.igra.is_a_draw:
                self.obvestilo.config(text='WINNER IS ' + self.igra.move + '!')
                self.koncaj()
            elif self.igra.is_a_draw:
                self.obvestilo.config(text='DRAW')
                self.koncaj()

    def koncaj(self):
        for i in range(3):
            for j in range(3):
                self.gumbi[i][j].config(state='disabled')
        
        

okno = tk.Tk()
Vmesnik(okno)
okno.mainloop()
                    



