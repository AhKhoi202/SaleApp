from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product
from app import app, db
from flask_admin import Admin, BaseView, expose

admin = Admin(app=app, name=' QUAN TRI BAN HANG',template_mode='bootstrap4')

class MyProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name','price']
    can_export = True
    edit_modal = True

class MyCategoryView(ModelView):
    column_list = ['name', 'products']


class MyStatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name="THONG KE BAO CAO"))
