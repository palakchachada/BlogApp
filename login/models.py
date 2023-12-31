from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, user_id,name, password,**extra_fields):
        if not user_id:
            raise ValueError("vendor_id Must Be Provided")
        if not password:
            raise ValueError("Password Must Be Provided")    
 
        user = self.model(
            user_id = user_id,
            name = name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using  = self.db)
        return user

    def create_user(self, user_id,name, password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(user_id,name,password,**extra_fields)    
    
    def create_superuser(self, user_id,name, password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(user_id,name,password,**extra_fields)    


# Create your models here.
class Post(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255,default ='')
    mobile_number = models.TextField(default ='',max_length=10)
    address = models.TextField(default ='')
    user_id = models.CharField(max_length=50, unique=True,default ='')
    title1 = models.CharField(max_length=255)
    content1 = models.TextField(default = '')
    pub_date = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_user = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name','address','mobile_number']


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __str__(self):
        return f'{self.name}'  
    


class AdminBlogs(models.Model):
    title = models.CharField(max_length=240,blank=True,null=True) 
    content =  models.TextField(null=True)
    date  = models.CharField(max_length=240,blank=True,null=True)

    def __str__(self):
        return f'{self.title}' 