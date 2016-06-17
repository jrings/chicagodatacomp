FROM ubuntu
MAINTAINER Joerg Rings <mail@rings.de>

# Install the Ubuntu packages.
RUN apt-get update --fix-missing
RUN apt-get install -y git python3 

RUN rm /usr/bin/python; ln -s /usr/bin/python3 /usr/bin/python

RUN apt-get install -y python3-pip cython python3-numpy python3-pytest python3-nose wget vim libfreetype6-dev libfreetype6 libpng-dev libblas-dev liblapack-dev
RUN rm /usr/bin/pip; ln -s /usr/bin/pip3 /usr/bin/pip

# Set the locale.
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# More environment variables.
ENV LD_LIBRARY_PATH /usr/local/lib
WORKDIR /home

# Install GEOS.
RUN wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
RUN tar -xjf geos-3.4.2.tar.bz2
RUN cd geos-3.4.2; ./configure --enable-debug; make; make install

# Install GDAL.
RUN wget http://download.osgeo.org/gdal/1.11.0/gdal-1.11.0.tar.gz
RUN tar -xzf gdal-1.11.0.tar.gz
RUN cd gdal-1.11.0; ./configure --enable-debug; make; make install

# Clone Shapely and install locally.
RUN git clone https://github.com/Toblerity/Shapely.git
RUN cd Shapely; pip install -e .

RUN pip install geojson ipython pyzmq jupyter folium
RUN ln -s /usr/include/freetype2/ft2build.h /usr/include/
RUN pip install matplotlib seaborn numpy scipy
RUN apt-get install -y python-setuptools python3-setuptools
RUN rm /usr/bin/pip; ln -s /usr/bin/pip3 /usr/bin/pip
RUN git clone -v https://github.com/matplotlib/basemap.git
RUN rm /usr/bin/python; ln -s /usr/bin/python3 /usr/bin/python
RUN rm /usr/bin/pip; ln -s /usr/bin/pip3 /usr/bin/pip
RUN cd basemap; python setup.py install
RUN pip install descartes pyproj
RUN git clone https://github.com/sjsrey/pysal.git
RUN cd pysal; git checkout py3merge; python setup.py install

RUN git clone https://github.com/geopandas/geopandas.git
RUN cd geopandas; python setup.py install

RUN pip install sklearn line_profiler netCDF4 docopt

RUN git clone https://github.com/coagulant/progressbar-python3
RUN cd progressbar-python3; python setup.py install

RUN mkdir -p -m 700 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py

VOLUME /data
WORKDIR /data

EXPOSE 8888

