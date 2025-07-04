import subprocess

def get_reference(doi):
    # initialize strings
    ref=""
    ref_url=""
    # retrieve citation from doi
    if(len(doi)>0):
      # check if unpublished/submitted
      if(doi.lower()=="unpublished" or doi.lower()=="submitted"):
        ref=doi.lower()
      # get info from doi
      else: 
        # get citation
        cit = subprocess.check_output('curl -LH "Accept: text/bibliography; style=science" \'http://dx.doi.org/'+doi+'\'', shell=True).decode('utf-8').strip()
        if("DOI Not Found" in cit):
         ref="DOI not found"
        else:
         # get citation
         ref=cit[3:cit.find(", doi")]
         # and url
         ref_url="http://dx.doi.org/"+doi
    return ref,ref_url

def print_references( dois, f ) : 
    for doi in dois :
        ref, ref_url = get_reference(doi)
        f.write("- [" + ref + "](" + ref_url + ")\n")

if __name__ == "__main__" :
   with open("reading_list.md","w+") as f : 
        f.write("# Reading list for CCP5 Summer School\n\n")
        f.write("## Software and tutorials\n\n" )
        f.write("- [PLUMED code](www.plumed.org) PLUMED code for doing free energy calculations\n")
        f.write("- [PLUMED tutorials](www.plumed-tutorials.org) Tutorials on using PLUMED code\n")
        f.write("- [PLUMED nest](www.plumed-nest.org) Examples of calculations people have done with PLUMED\n")
        f.write("\n## Background theory\n\n")
        print_references(["10.1007/978-1-4939-9608-7_21", "10.1016/j.cpc.2013.09.018" ], f )
        f.write("\n## Metadynamics\n\n")
        print_references(["10.1073/pnas.202427399","10.1103/PhysRevLett.100.020603","10.1038/s42254-020-0153-0","10.1063/1.5123498"], f )
        f.write("\n## Transition path sampling and transition interface sampling\n\n")
        print_references(["10.1146/annurev.physchem.53.082301.113146", "10.1016/j.physa.2004.04.033"], f )
        f.write(" - [Open path sampling ](http://openpathsampling.org/latest/) code for using these methods\n")
        f.write("\n## Path collective variables\n\n")
        print_references(["10.1063/1.2432340", "10.1103/PhysRevLett.109.020601"], f )
        f.write("\n## Kinetics from biased simulations\n\n")
        print_references(["10.1103/PhysRevLett.78.3908", "10.1103/PhysRevLett.111.230602"], f ) 
        f.write("\n## Metadynamics for nucleation\n\n")
        print_references(["10.1103/PhysRevB.92.180102", "10.1063/1.4997180", "10.1063/1.5134461", "10.1088/1361-648X/aa893d"], f )

