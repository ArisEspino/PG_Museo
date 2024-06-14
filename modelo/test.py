import os
import vtk

def main():
    # Ruta
    absolute_file_path = 'C:/Users/kelly vallecillo/Downloads/PG_Museo/modelo/thismuseo.obj'

    #this is for know about the object status
    if not os.path.isfile(absolute_file_path):
        print(f"Error: El archivo {absolute_file_path} no existe.")
        return

    if os.path.getsize(absolute_file_path) == 0:
        print(f"Error: El archivo {absolute_file_path} está vacío.")
        return

    print(f"Archivo {absolute_file_path} encontrado y no está vacío.")

    # this is the reader
    reader = vtk.vtkOBJReader()
    reader.SetFileName(absolute_file_path)

    # checking the reader
    reader.Update()
    if reader.GetOutput().GetNumberOfPoints() == 0:
        print(f"Error: No se pudo leer el archivo {absolute_file_path} o el archivo está vacío.")
        return
    else:
        print(f"Archivo {absolute_file_path} leído correctamente.")

    # building a map
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # building an actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # building a  renderer
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(1.0, 0.75, 0.8)  # screen color

    # camera and mouse
    camera = renderer.GetActiveCamera()
    camera.SetPosition(0, 0, 10)
    camera.SetFocalPoint(0, 0, 0)
    camera.SetViewUp(0, 1, 0)
    #camera and window
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetSize(800, 800)    # window size
    render_window.SetWindowName("Modelo Ejemplo")


    style = vtk.vtkInteractorStyleTrackballCamera()
    style.SetCurrentRenderer(renderer)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetInteractorStyle(style)
    interactor.SetRenderWindow(render_window)

    # open the window and start to rendering
    render_window.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
