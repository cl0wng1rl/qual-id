set -e

INSTALL_DIR="${1:-.}"
REPO="https://api.github.com/repos/gabrielbarker/qual-id/releases/latest"
URL=$(curl -s "$REPO"|grep '"browser_download_url":'|sed -E 's/.*"([^"]+)".*/\1/')
TAG=$(curl -s "$REPO"|grep '"tag_name":'|sed -E 's/.*"([^"]+)".*/\1/')
TAR_NAME=latest.tar.gz
echo "Downloading $TAG..."
curl -s -L $URL > $INSTALL_DIR/$TAR_NAME
tar -zxf $INSTALL_DIR/$TAR_NAME
echo "Installing $TAG..."
rm $INSTALL_DIR/$TAR_NAME
mv $TAG $INSTALL_DIR/
rm -rf $INSTALL_DIR/qual_id
mv $INSTALL_DIR/$TAG/qual_id $INSTALL_DIR/qual_id
mv $INSTALL_DIR/$TAG/qid $INSTALL_DIR/qid
rm -rf $INSTALL_DIR/$TAG
echo "Done!"
