using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Windows.Forms;

[assembly: AssemblyTitle("Pratice Code")]
[assembly: AssemblyDescription("Offline study workspace launcher")]
[assembly: AssemblyVersion("1.1.0.0")]
internal static class Launcher {
    [STAThread] private static int Main(string[] args) {
        try {
            string root=AppDomain.CurrentDomain.BaseDirectory;
            string runtime=Path.Combine(root,"runtime","python.exe");
            if(!File.Exists(runtime))throw new IOException("The bundled runtime is missing. Please reinstall Pratice Code.");
            string command="\""+Path.Combine(root,"launch.py")+"\"";
            foreach(string arg in args) {
                if(arg.IndexOf('"')>=0)throw new ArgumentException("Invalid launcher argument.");
                command+=" \""+arg+"\"";
            }
            var info=new ProcessStartInfo(runtime,command) {WorkingDirectory=root,UseShellExecute=false,CreateNoWindow=true,RedirectStandardOutput=true,RedirectStandardError=true};
            using(var process=Process.Start(info)) {
                string output=process.StandardOutput.ReadToEnd();
                string errors=process.StandardError.ReadToEnd();
                process.WaitForExit();
                if(process.ExitCode!=0)throw new IOException(output+Environment.NewLine+errors);
                return 0;
            }
        } catch(Exception error) {
            MessageBox.Show(error.Message,"Pratice Code",MessageBoxButtons.OK,MessageBoxIcon.Error);return 1;
        }
    }
}
