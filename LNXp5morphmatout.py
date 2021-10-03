import bpy  
import os
import bmesh

#pick one, or put your own!
#frames = range(610,615)
#frames = [2050,2055,2060,2065,2070,2075,2080]
#frames = range(2050,2080,5)#have to add 'step' to last frame to process it, but for anim loops omitting this is convenient
frames =[1270,1280,1350,1370,1390,1485,1495,1505,1515,1950,1960,1970,1980,1990,2005,2015,2025,2035,2050,2055,2060,2065,2070,2075,2260,2270,2280,2290,2450,2460,2470,2480,2490,2515,2525,2535,2545,2555,2875,2885,2895,3110,3160,3170,3235,3245,3255,3265,3275,4150,4155,4160,4165,4170,4175,4180,4185,4190,4195,4200,4220,4230,4240,4250,4260,4270,4280]
#frames = range(2050,2080,5)#have to add 'step' to last frame to process it, but for anim loops omitting this is convenient


depgraph = bpy.context.evaluated_depsgraph_get()

main_path = "/home/victor/output/"
print("writing to: " + main_path + "\n\n")

outputfile = os.path.join(main_path, 'uv5sldanim.dat')
w_file=open(outputfile, 'w')
n=0  
obj = bpy.context.active_object


print("verts, "+str(len(obj.data.vertices)))  
w_file.write("verts, "+str(len(obj.data.vertices))+"\n")
for v in obj.data.vertices:
    w_file.write(format(n,'1d')+', '+format(v.co.x,'.3f')+", "+format(v.co.y,'.3f')+", "+format(v.co.z,'.3f')+" \n")  
    n+=1
w_file.write("vnorm,"+str(len(obj.data.vertices))+"\n")
vc=0  
for v in obj.data.vertices:  
    w_file.write(str(vc)+", "+format(v.normal.x,'.5f')+','+format(v.normal.y,'.5f')+','+format(v.normal.z,'.5f')+" \n") 
    vc+=1

print("faces, "+str(len(obj.data.polygons)))  
w_file.write("faces, "+str(len(obj.data.polygons))+"\n")
fc=0;  
for i in obj.data.polygons:
    vid = i.vertices[:]  
    #	print(verts_on_face)  
    w_file.write(str(fc)+", "+format(vid[0],'1d')+", "+format(vid[1],'1d')+", "+format(vid[2],'1d')+"  \n")
    fc+=1
#referenced from:https://odederell3d.blog/2020/09/28/blender-python-accessing-uv-data/
mesh_data = obj.data
mesh_loops = mesh_data.loops
uv_index = 0


#iterate mesh loops:
for lp in mesh_loops:
# access uv loop:
    uv_loop = mesh_data.uv_layers[uv_index].data[lp.index]
    uv_coords = uv_loop.uv
    vid=lp.vertex_index
    vert=obj.data.vertices
    #print('uvxyz: {0},'.format(lp.vertex_index))
    #print('U:{0:1.5f}, V:{1:1.5f}' .format(uv_coords[0], uv_coords[1]))
    #print('X:{0:1.5f}, Y:{1:1.5f}, Z:{2:1.5f}, ' .format(vert[vid].co.x, vert[vid].co.y, vert[vid].co.z))
    w_file.write("iduvxyz, "+str(lp.vertex_index)+', ')
    w_file.write(format(uv_coords[0],'.5f')+", "+format(uv_coords[1],'.5f')+", ")
    w_file.write(format(vert[vid].co.x,".5f")+", "+format(vert[vid].co.y,".5f")+", "+format(vert[vid].co.z,".5f")+"\n")
    
#    w_file.write("uvxyz["+str(lp.vertex_index)+"]: "+format(uv_coords[0],'.5f')+", "+format(uv_coords[1],'.5f')+', #'+format(vert[vid].co.x,".5f")+", "+format(vert[vid].co.y,".5f")+", "+format(vert[vid].co.z,".5f")+"\n")

w_file.write("face material list\n")
for f in obj.data.polygons:  # iterate over faces build
    slot = obj.material_slots[f.material_index]
    mat = slot.material
    if mat is not None:
        w_file.write(format(f.material_index,'d')+", "+format(f.index,'d')+","+mat.name+"\n")
        #print(format(f.material_index,'d')+", "+format(f.index,'d')+", "+"("+mat.name+")")
    #else:
    #    print("none", f.material_index)
    #print("face", f.index, "material_index", f.material_index)


#referenced from https://odederell3d.blog/2020/09/28/blender-python-access-animated-vertices-data/    
fno=0;
for f in frames:
    fno+=1
    print("frame "+str(f)+" of "+ str(frames[-1]))
    bpy.context.scene.frame_set(f)
    bm = bmesh.new()
    bm.verts.ensure_lookup_table()
# read the evaluated mesh data into the bmesh   object:
    bm.from_object( obj, depgraph )
    w_file.write("frame, "+str(f)+", "+str(fno)+", "+str(len(frames))+"\n")
# iterate the bmesh verts:
    for x, v in enumerate(bm.verts):
        w_file.write(str(x)+", "+format(v.co.x,".5f")+", "+format(v.co.y,".5f")+", "+format(v.co.z,".5f")+" \n")
        
    bm.free()


w_file.close()
print("finished!\n")
