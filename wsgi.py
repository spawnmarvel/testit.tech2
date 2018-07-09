from app import create_app


dv = "development"
pr = "production"

app = create_app(dv)

if __name__ =="__main__":
   print("\n Success, system path jekl")
   app.run()
