cd ../..; #cd to /
sudo cp /root/cicada/ng_conf /etc/nginx/sites-available/ng_conf; #copies custom nginx file
sudo ln -s /etc/nginx/sites-available/ng_conf /etc/nginx/sites-enabled/ng_conf; #symlink the new file
sudo service nginx configtest; #check config
sudo service nginx restart; #restart nginx
cd /root/cicada; #cd to cicada
docker build -t dock_img .; #create docker image
docker run -p 8080:8080 dock_img; #run docker image