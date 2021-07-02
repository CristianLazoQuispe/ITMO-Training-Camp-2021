#include<bits/stdc++.h>

using namespace std;

struct point{
    double x, y;
    point(double x_, double y_) : x(x_),y(y_){}

    point operator+(point other){
        return point(x +other.x,y +other.y);
    }
    point operator-(point other){
        return point(x-other.x,y-other.y);
    }

    double len(){
        return sqrt(x*x+y*y);
    }

};
ostream& operator<<(ostream& o, point p){
    o<< "(" << p.x<<", "<<p.y<<")";
    return o;
};
double cross(point p1, point p2){
    return p1.x*p2.y - p1.y*p2.x;
}
double dot(point p1, point p2){
    return p1.x*p2.x + p1.y*p2.y;
}

double angle_between_vectors(point v1, point v2){
    return atan2(cross(v1,v2),dot(v1,v2));
}


double triangle_area(point a, point b, point c){
    point v1 = b-a;
    point v2 = c-a;
    return abs(cross(v1,v2)/2);
}

double area_of_polygon(vector<point> poly){
    double s=0;
    //cout<<" size of "<< poly.size()<<"\n";
    for (int i=0;i<poly.size();i++){
        int next = (i+1)% poly.size();
        s+= cross(poly[i],poly[next]);
    }
    return abs(s/2);
}


struct line{
    double a,b,c;
    line(point p1,point p2){
        a = p2.y - p1.y;
        b = p1.x - p2.x;
        c = -(a*p1.x + b*p1.y);
        assert(abs(a*p2.x + b*p2.y +c)<= 1e-9);
        double tmp = sqrt(a*a+b*b);
    }

    double dist(point p){
        return a*p.x+b*p.y+c;
    }
    
};
bool is_parallel(line l1, line l2){
    return abs(l1.a*l2.b - l1.b*l2.a)<=1e-9;
}
point intersection(line l1, line l2){
    double d = l1.a*l2.b - l1.b*l2.a;
    double nx = -l1.c*l2.b + l1.b*l2.c;
    double ny = -l1.a *l2.c + l1.c*l2.a;
    return point(nx/d,ny/d);
}
int main(){

    double x1,y1;
    int n;
    vector<point> poligono;
    std::cout << std::setprecision(7);
    cin>>n;
    //cout<<" n "<<n<<"\n";
    for (int i=0;i<n;i++){
        cin>>x1>>y1;
        //cout<<x1<<" "<<y1<<"\n";

        poligono.push_back(point(x1,y1));
    }
    cout<<abs(area_of_polygon(poligono))<<"\n";

}
