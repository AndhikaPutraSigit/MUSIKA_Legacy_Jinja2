from flask import Flask, render_template, request, redirect, url_for, abort
import re
app = Flask(__name__)
TERDAFTAR = ['andhika', 'farid', 'cindu', 'admin']
PRODUK = [
 {'id':1,'nama':'Electric Guitar','harga':2500000,'kategori':'Guitar','deskripsi':'Gitar elektrik untuk musik modern.'},
 {'id':2,'nama':'Acoustic Guitar','harga':1800000,'kategori':'Guitar','deskripsi':'Gitar akustik dengan suara natural.'},
 {'id':3,'nama':'Bass Guitar','harga':3000000,'kategori':'Bass','deskripsi':'Bass sebagai fondasi ritme musik.'},
 {'id':4,'nama':'Drum Set','harga':5500000,'kategori':'Percussion','deskripsi':'Set drum untuk permainan dinamis.'},
 {'id':5,'nama':'Keyboard','harga':4000000,'kategori':'Keyboard','deskripsi':'Keyboard untuk berbagai kebutuhan musikal.'},
 {'id':6,'nama':'Amplifiers','harga':2200000,'kategori':'Audio','deskripsi':'Amplifier untuk memperkuat suara instrumen.'}]
@app.route('/')
def index(): return render_template('index.html')
@app.route('/tentang')
def tentang(): return render_template('tentang.html')
@app.route('/produk')
def produk(): return render_template('produk.html', produk=PRODUK)
@app.route('/produk/<int:id>')
def detail_produk(id):
 p=next((x for x in PRODUK if x['id']==id),None)
 if p is None: abort(404)
 return render_template('detail_produk.html', produk=p)
@app.route('/kontak')
def kontak(): return render_template('kontak.html')
@app.route('/cek', methods=['GET','POST'])
def cek_username():
 username=''; hasil=None
 if request.method=='POST':
  username=request.form.get('username','').strip()
  if not re.fullmatch(r'[A-Za-z0-9_]{4,20}',username): hasil='tidak_valid'
  elif username.lower() in TERDAFTAR: hasil='dipakai'
  else: hasil='tersedia'
 return render_template('cek.html', username=username, hasil=hasil)
@app.route('/member', methods=['GET','POST'])
def member():
 pesan=None
 if request.method=='POST':
  username=request.form.get('username','').strip()
  if not re.fullmatch(r'[A-Za-z0-9_]{3,20}',username): pesan='Username harus 3–20 karakter: huruf, angka, atau underscore.'
  else: return redirect(url_for('user_profile', username=username))
 return render_template('member.html', pesan=pesan)
@app.route('/user/<username>')
def user_profile(username): return render_template('user.html', username=username)
@app.errorhandler(404)
def not_found(error): return render_template('404.html'),404
if __name__=='__main__': app.run(debug=True)
