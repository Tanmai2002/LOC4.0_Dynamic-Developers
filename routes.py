from genericpath import exists
from multiprocessing.connection import wait
from werkzeug.utils import secure_filename
import img_enhancer_module.enhance_my_img as enhanceImg
import cv2.cv2 as cv
from func import removeBack,bw2color
# from werkzeug.datastructures import  FileStorage
import os
import secrets
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from forms import VideoForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '15de991f5f224a1d524d408efc1753ac'

# path = os.getcwd()
# UPLOAD_FOLDER = os.path.join(path, 'uploads')
# if not os.path.isdir(UPLOAD_FOLDER):
#     os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static\images')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('home.html', title='Home')

# def save_video(form_video):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.split(form_video.filename)
#     video_fn = random_hex + f_ext
#     video_path = os.path.join(app.root_path, 'static/videos', video_fn)
#     form_video.save(video_path)
#     return video_fn

@app.route('/')
@app.route('/upload', methods=['GET','POST'])
def upload():
    form = VideoForm()
    if request.method == 'POST':
        i=0
        for f in request.files.getlist('file_name'):
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f'test0.jpg'))
            # detect.getmarkedVideo(os.path.join(app.config['UPLOAD_FOLDER'], f'test{i}.mp4'))
        # return render_template('videos.html', title='Video',test1='images/test0.jpg')
        return render_template('demopg/Effects.html', title='Effects',test1='images/test0.jpg')
        # return render_template('upload.html', msg="File(s) have been uploaded successfully")
    return render_template('upload.html', title='upload',form=form, msg="Please Choose files")


@app.route('/')
@app.route('/filters', methods=['GET','POST'])
@app.route('/filters')
def filters():
    return render_template('demopg/filters.html', title='Filters',test1='images/test0.jpg')

@app.route('/')
@app.route('/features', methods=['GET','POST'])
@app.route('/features')
def features():
    return render_template('features.html', title='Features',test1='images/test0.jpg')


@app.route('/')
@app.route('/saveAndMove', methods=['GET','POST'])
@app.route('/saveAndMove')
def saveAndMove():
    
    return render_template('features.html', title='Features',test1='images/test0.jpg')




@app.route('/')
@app.route('/analysis')
def analysis():
    g1="g1"
    g2='g2'
    return render_template('Analysis.html', test1=g1,test2=g1,test3=g2,test4=g2)
    # return render_template('analysis.html', title='Analysis')

@app.route('/')
@app.route('/filterA', methods=['GET','POST'])
def filterA():
    if request.method == 'POST':
        
        img=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'))
        img2=img.copy()
        if 'filterPix' in request.form:
            img2=enhanceImg.Pixalete(cv.cvtColor(img,cv.COLOR_BGR2RGB))
        if 'filterRemoveB' in request.form:
            img2=enhanceImg.plainRGB(img,0)
        if 'filterRemoveR' in request.form:
            img2=enhanceImg.plainRGB(img,1)
        if 'filterRemoveG' in request.form:
            img2=enhanceImg.plainRGB(img,2)
        if 'filterUnsharpMask' in request.form:
            img2=enhanceImg.filter1(cv.cvtColor(img,cv.COLOR_BGR2RGB),0)
        if 'filterSMOOTH' in request.form:
            img2=enhanceImg.filter1(cv.cvtColor(img,cv.COLOR_BGR2RGB),1)
        if 'filterDETAIL' in request.form:
            img2=enhanceImg.filter1(cv.cvtColor(img,cv.COLOR_BGR2RGB),2)
        
        cv.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], 'test1.jpg'),img2)
        
        return render_template('demopg/filters.html', title='Home',test1='images/test1.jpg')




@app.route('/')
@app.route('/featuresA', methods=['GET','POST'])
def featuresA():
    if request.method == 'POST':
        
        img=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'))
        img2=img.copy()
        
        if 'XfilterPix' in request.form:
            img2=enhanceImg.Pixalete(cv.cvtColor(img,cv.COLOR_BGR2RGB))
            removeBack(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            imt=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            img2=enhanceImg.mergeWithFilter(imt,img2)
        
        if 'XfilterRemoveB' in request.form:
            img2=enhanceImg.plainRGB(img,0)
            removeBack(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            imt=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            img2=enhanceImg.mergeWithFilter(imt,img2)
        
        if 'XfilterRemoveR' in request.form:
            img2=enhanceImg.plainRGB(img,1)
            removeBack(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            imt=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            img2=enhanceImg.mergeWithFilter(imt,img2)
        
        if 'XfilterRemoveG' in request.form:
            img2=enhanceImg.plainRGB(img,2)
            removeBack(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            imt=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            img2=enhanceImg.mergeWithFilter(imt,img2)
        
        if 'XfilterUnsharpMask' in request.form:
            img2=enhanceImg.filter1(cv.cvtColor(img,cv.COLOR_BGR2RGB),0)
            removeBack(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            imt=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            img2=enhanceImg.mergeWithFilter(imt,img2)
        
        if 'XfilterSMOOTH' in request.form:
            img2=enhanceImg.filter1(cv.cvtColor(img,cv.COLOR_BGR2RGB),1)
            removeBack(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            imt=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            img2=enhanceImg.mergeWithFilter(imt,img2)

        if 'XfilterNEG' in request.form:
            img2=enhanceImg.defFilters(img,1)
            removeBack(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            imt=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            img2=enhanceImg.mergeWithFilter(imt,img2)
        if 'BgRemove' in request.form:
            removeBack(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            img2=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'no-back.png'))
            cv.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], 'test2.png'),img2)
            return render_template('features.html', title='Features',test1='images/test2.png')
        if 'BW2C' in request.form:
            bw2color(os.path.join(app.config['UPLOAD_FOLDER'], 'test0.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'no-back1.png'))
            imt=cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'no-back1.png'))
            img2=enhanceImg.mergeWithFilter(imt,img2)
        cv.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], 'test1.jpg'),img2)
        
        return render_template('features.html', title='Features',test1='images/test1.jpg')


