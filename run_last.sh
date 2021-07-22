cd ../..; #cd to /
sudo cp /root/your_repo_root_folder/ng_conf /etc/nginx/sites-available/ng_conf; #copies custom nginx file, remember to replace your_repo_root_folder with appropriate name for your event
sudo ln -s /etc/nginx/sites-available/ng_conf /etc/nginx/sites-enabled/ng_conf; #symlink the new file
sudo service nginx configtest; #check config
sudo service nginx restart; #restart nginx
cd /root/your_repo_root_folder; #cd to your_rep_root_folder, remember to replace it
docker build -t dock_img .; #create docker image
docker run -p 8080:8080 dock_img; #run docker image
