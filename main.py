from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os

class IMG_Stegno:
    def main(self,root):
        root.title('ImageSteganography')
        root.geometry('400x500')
        root.resizable(width =False, height=False)
        root.config(bg = '#0B2447')
        frame = Frame(root)
        frame.grid()

        title = Label(frame,text='Image Steganography')
        title.config(font=('Times new roman',25, 'bold'),bg = '#0B2447',fg='#A5D7E8',justify=CENTER)
        #title.grid(pady=10)
        title.grid(row=1)

        LSB=Button(frame,text="LSB",command= lambda :self.LSB(frame), padx=14,bg = '#19376D' )
        LSB.config(font=('Helvetica',14), bg='#576CBC')
        LSB.grid(row=2,pady=10)

        PVD=Button(frame,text="PVD",command= lambda :self.PVD(frame), padx=14,bg = '#19376D' )
        PVD.config(font=('Helvetica',14), bg='#576CBC')
        PVD.grid(row=3,pady=10)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)        

    #Back function to loop back to main screen
    def back(self,frame):
        frame.destroy()
        self.main(root)

#---------------------------------------------------------------------------------------------------------------#

    #Frame for LSB page
    def LSB(self,p_f):
        p_f.destroy()
        p_f2 = Frame(root)
        encode = Button(p_f2,text="Encode",command= lambda :self.encode_frame1(p_f2), padx=14,bg = '#19376D' )
        encode.config(font=('Helvetica',14), bg='#576CBC')
        encode.grid(row=2)
        decode = Button(p_f2, text="Decode",command=lambda :self.decode_frame1(p_f2), padx=14,bg = '#19376D')
        decode.config(font=('Helvetica',14), bg='#576CBC')
        decode.grid(pady = 12)
        decode.grid(row=3)
        button_back = Button(p_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,p_f2))
        button_back.config(font=('Helvetica',18),bg='#576CBC')
        button_back.grid(pady=15)
        button_back.grid()
        p_f2.grid()

    #frame for LSB encode page
    def encode_frame1(self,F):
        F.destroy()
        F2 = Frame(root)
        label1= Label(F2,text='Select the Image in which \n you want to hide text :')
        label1.config(font=('Times new roman',25, 'bold'),bg = '#19376D',fg='#A5D7E8')
        label1.grid()
 
        button_bws = Button(F2,text='Select',command=lambda : self.encode_frame2(F2))
        button_bws.config(font=('Helvetica',18), bg='#576CBC')
        button_bws.grid()
        button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self,F2))
        button_back.config(font=('Helvetica',18),bg='#576CBC')
        button_back.grid(pady=15)
        button_back.grid()
        F2.grid()
 
#frame for LSB decode page
    def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Times new roman',25,'bold'),bg = '#19376D',fg='#A5D7E8')
        label1.grid()
        label1.config(bg = '#19376D')
        button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
        button_bws.config(font=('Helvetica',18), bg='#576CBC')
        button_bws.grid()
        button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
        button_back.config(font=('Helvetica',18), bg='#576CBC')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()
    
    # LSB function to encode image
    def encode_frame2(self,e_F2):
        e_pg= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300,200))
            img = ImageTk.PhotoImage(new_image)
            label3= Label(e_pg,text='Selected Image')
            label3.config(font=('Helvetica',14,'bold'))
            label3.grid() 
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()
            label2 = Label(e_pg, text='Enter the message')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=15)
            text_a = Text(e_pg, width=50, height=10)
            text_a.grid()
            encode_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self,e_pg))
            encode_button.config(font=('Helvetica',14), bg='#576CBC')
            data = text_a.get("1.0", "end-1c")
            button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img),IMG_Stegno.back(self,e_pg)])
            button_back.config(font=('Helvetica',14), bg='#576CBC')
            button_back.grid(pady=15)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F2.destroy()

    # LSB function to decode image
    def decode_frame2(self,d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(d_F3,text='Selected Image :')
            label4.config(font=('Helvetica',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            label2 = Label(d_F3, text='Hidden data is :')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command= lambda :IMG_Stegno.back(self,d_F3))
            button_back.config(font=('Helvetica',14),bg='#576CBC')
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()
    
    #LSB function to decode data
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''
 
        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            # string of binary data
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'
 
            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data
            
    #LSB function to generate data
    def generate_Data(self,data):
        # list of binary codes of given data
        new_data = []
 
        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data

    #LSB function to modify the pixels of image
    def modify_Pix(self,pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
 
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1
 
                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
                    if (i == dataLen - 1):
                        if (pix[-1] % 2 == 0):
                            pix[-1] -= 1
                    else:
                        if (pix[-1] % 2 != 0):
                            pix[-1] -= 1
 
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    
    #LSB function to enter the data pixels in image
    def encode_enc(self,newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)
 
        for pixel in self.modify_Pix(newImg.getdata(), data):
 
            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    #LSB function to enter hidden text
    def enc_fun(self,text_a,myImg):
        data = text_a.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename (initialfile=temp, filetypes = ([('png', '*.png')]), defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

    def frame_3(self,frame):
        frame.destroy()
        self.main(root)

#---------------------------------------------------------------------------------------------------------------#
    #Frame for LSB page
    def PVD(self,p_f):
        p_f.destroy()
        p_f2 = Frame(root)
        encode = Button(p_f2,text="Encode",command= lambda :self.encode_pvd(p_f2), padx=14,bg = '#19376D' )
        encode.config(font=('Helvetica',14), bg='#576CBC')
        encode.grid(row=2)
        decode = Button(p_f2, text="Decode",command=lambda :self.decode_pvd(p_f2), padx=14,bg = '#19376D')
        decode.config(font=('Helvetica',14), bg='#576CBC')
        decode.grid(pady = 12)
        decode.grid(row=3)
        button_back = Button(p_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,p_f2))
        button_back.config(font=('Helvetica',18),bg='#576CBC')
        button_back.grid(pady=15)
        button_back.grid()
        p_f2.grid()

    #frame for LSB encode page
    def encode_pvd(self,F):
        F.destroy()
        F2 = Frame(root)
        label1= Label(F2,text='Select the Image in which \n you want to hide text :')
        label1.config(font=('Times new roman',25, 'bold'),bg = '#19376D',fg='#A5D7E8')
        label1.grid()
 
        button_bws = Button(F2,text='Select',command=lambda : self.encode_pvd1(F2))
        button_bws.config(font=('Helvetica',18), bg='#576CBC')
        button_bws.grid()
        button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self,F2))
        button_back.config(font=('Helvetica',18),bg='#576CBC')
        button_back.grid(pady=15)
        button_back.grid()
        F2.grid()
 
    #frame for LSB decode page
    def decode_pvd(self,F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Times new roman',25,'bold'),bg = '#19376D',fg='#A5D7E8')
        label1.grid()
        label1.config(bg = '#19376D')
        button_bws = Button(d_f2, text='Select', command=lambda :self.decode_pvd1(d_f2))
        button_bws.config(font=('Helvetica',18), bg='#576CBC')
        button_bws.grid()
        button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
        button_back.config(font=('Helvetica',18), bg='#576CBC')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()

    # LSB function to encode image
    def encode_pvd1(self,e_F2):
        e_pg= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300,200))
            img = ImageTk.PhotoImage(new_image)
            label3= Label(e_pg,text='Selected Image')
            label3.config(font=('Helvetica',14,'bold'))
            label3.grid() 
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()
            label2 = Label(e_pg, text='Enter the message')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=15)
            text_a = Text(e_pg, width=50, height=10)
            text_a.grid()
            encode_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self,e_pg))
            encode_button.config(font=('Helvetica',14), bg='#576CBC')
            data = text_a.get("1.0", "end-1c")
            print(data)
            button_back = Button(e_pg, text='Encode', command=lambda : [self.encode_pvd_fun(myfile,text_a.get("1.0","end")),IMG_Stegno.back(self,e_pg)])
            button_back.config(font=('Helvetica',14), bg='#576CBC')
            button_back.grid(pady=15)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F2.destroy()

    #PVD function to encode Data
    def encode_pvd_fun(self,image_path, secret_msg):
        image = Image.open(image_path)
        width, height = image.size
        pixel_values = list(image.getdata())

        # Check if the secret message fits in the image
        msg_bits = ''.join(format(ord(i), '08b') for i in secret_msg)
        if len(msg_bits) > len(pixel_values) * 3:
            raise ValueError("Secret message too large for the image")

        # Embed the secret message
        msg_bits += '00000000'  # Add null terminator
        msg_idx = 0
        for i in range(len(pixel_values) - 1):
            if msg_idx >= len(msg_bits):
                break
            r_diff = abs(pixel_values[i][0] - pixel_values[i+1][0])
            g_diff = abs(pixel_values[i][1] - pixel_values[i+1][1])
            b_diff = abs(pixel_values[i][2] - pixel_values[i+1][2])

            # Modify the LSB of the difference value
            if msg_bits[msg_idx] == '1':
                r_diff |= 1
            else:
                r_diff &= ~1
            msg_idx += 1
            if msg_bits[msg_idx] == '1':
                g_diff |= 1
            else:
                g_diff &= ~1
            msg_idx += 1
            if msg_bits[msg_idx] == '1':
                b_diff |= 1
            else:
                b_diff &= ~1
            msg_idx += 1

            # Embed the modified difference values into the pixels
            if pixel_values[i][0] < pixel_values[i+1][0]:
                pixel_values[i] = (pixel_values[i][0] + r_diff, pixel_values[i][1], pixel_values[i][2])
            else:
                pixel_values[i] = (pixel_values[i][0] - r_diff, pixel_values[i][1], pixel_values[i][2])

            if pixel_values[i][1] < pixel_values[i+1][1]:
                pixel_values[i] = (pixel_values[i][0], pixel_values[i][1] + g_diff, pixel_values[i][2])
            else:
                pixel_values[i] = (pixel_values[i][0], pixel_values[i][1] - g_diff, pixel_values[i][2])

            if pixel_values[i][2] < pixel_values[i+1][2]:
                pixel_values[i] = (pixel_values[i][0], pixel_values[i][1], pixel_values[i][2] + b_diff)
            else:
                pixel_values[i] = (pixel_values[i][0], pixel_values[i][1], pixel_values[i][2] - b_diff)

        # Save the modified image
        encoded_image = Image.new("RGB", (width, height))
        encoded_image.putdata(pixel_values)
        encoded_image.save("encoded.png")
        messagebox.showinfo("Success","Encoding Successful\nFile is saved as encode.png in the same directory") 

    # PVD function to decode image
    def decode_pvd1(self,d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(d_F3,text='Selected Image :')
            label4.config(font=('Helvetica',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode_pvd_fun(myfiles)
            label2 = Label(d_F3, text='Hidden data is :')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command= lambda :IMG_Stegno.back(self,d_F3))
            button_back.config(font=('Helvetica',14),bg='#576CBC')
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()

    def decode_pvd_fun(self,image_path):
        img = Image.open(image_path)
        width, height = img.size
        
        binary_message = ""
        index = 0
        
        for y in range(height):
            for x in range(width):
                if index % 8 == 0:
                    if index > 0 and index // 8 == len(binary_message):
                        return bytes.fromhex(hex(int(binary_message, 2))[2:]).decode('latin-1')
                    pixel = img.getpixel((x, y))
                    for c in range(3):
                        if pixel[c] % 2 == 0:
                            binary_message += '0'
                        else:
                            binary_message += '1'
                index += 1
        
        return bytes.fromhex(hex(int(binary_message, 2))[2:]).decode('latin-1')

#GUI Loop
root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()