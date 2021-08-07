#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

ifstream::pos_type filesize(const char* filename)
{
    ifstream in(filename, ifstream::ate | ifstream::binary);
    return in.tellg(); 
}

int main(){
vector<vector<string>> daniel;

daniel.resize(filesize("data.txt"));
for(int i = 0; i<daniel.size(); i++)
{
    daniel[i].resize(4);
}

fstream readObject("data.txt");     
fstream writeObject("map_coordinates.txt");
size_t row_length = 0;
while(!readObject.eof()){
readObject>>daniel[row_length][0]>>daniel[row_length][1]>>daniel[row_length][2]>>daniel[row_length][3];
++row_length;
}
//Find Matches:
for(int j=0;j<row_length;++j) 
{
    for(int x=j+1; x<(row_length-j-1); ++x)
    {
        if(((daniel[j][0] != daniel[x][0]) || (daniel[j][1] != daniel[x][1])) && (daniel[j][3] == daniel[x][3]))
        {
            writeObject<<daniel[j][0]<<" "<<daniel[j][1]<<" "<<daniel[j][2]<<" "<<daniel[j][3]<<" "<<daniel[x][0]<<" "<<daniel[x][1]<<" "<<daniel[x][2]<<" "<<daniel[x][3]<<endl; 
        }
    }
}
cout<<"Done scanning!"<<endl;
readObject.close();
writeObject.close();






}