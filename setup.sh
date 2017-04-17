if [ ! -f "mxm_dataset.db" ]; then
    echo "downloading mxm database"
    wget http://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/mxm_dataset.db;
fi
if [ ! -f "msd_tagtraum_cd2c.cls" ]; then
    echo "downloading tagtraum annotations"
    wget http://www.tagtraum.com/genres/msd_tagtraum_cd2c.cls.zip;
    unzip msd_tagtraum_cd2c.cls.zip;
    rm msd_tagtraum_cd2c.cls.zip;
fi
if [ ! -f "mxm_779k_matches.txt" ]; then
    echo "downloading title mappings"
    wget http://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/mxm_779k_matches.txt.zip;
    unzip mxm_779k_matches.txt.zip;
    rm mxm_779k_matches.txt.zip;
fi
if [ ! -f "songs_input.txt" ]; then
    echo "reformatting data--could take a few minutes"
    python dataformat.py;
fi
