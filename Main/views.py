from django.db import transaction
from django.db.models import Q, Avg
from django.shortcuts import render

# Create your views here.
from openpyxl import load_workbook, Workbook
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from Main.models import ItemTable
from Main.serializers import ItemSerializer
from acelrtech_problem_solution.settings import BASE_DIR



def findParent(name):
    qs = None
    limit = 100
    i=0
    while 1:
        qss = ItemTable.objects.filter(Q(ItemCode__contains=name)|Q(ItemName__contains=name))
        print(qss)
        for qs in qss:
            print("qs ",qs.ParentCode)
            if qs.ParentCode == None:
                print(qs)
                return qs
            else:
                name = qs.ParentCode
        if i > limit:
            "break infinit loop if occurs"
            break
        i = i +1
    return qs

class ReadAPIView(ListAPIView):
    serializer_class = ItemSerializer
    # def get_queryset(self):
    #     qs = ItemTable.objects.all()
    #     return qs

    def get(self,request):
        try:
            option = int(self.request.GET.get('option', 0))
        except Exception as e:
            return Response({
                "Status":False,
                "Message":"Please provide intiger 0-4 "
            })
        name = self.request.GET.get('name', "")
        # print(option)
        if option in [0, 1, 2, 3, 4]:
            "by default option is 0 so list all products"
            qs = ItemTable.objects.all()

            if option == 1:
                "find top most parent "
                "API : http://127.0.0.1:8000/read/?option=1&name=AGNES-S"
                if not name or name == "":
                    return Response({
                        "Status": False,
                        "Message": "Required name"
                    })

                qs = findParent(name)
                return Response(ItemSerializer(qs).data)
                # qs =  qs.filter()

            elif option ==2:
                if not name or name=="":
                    return Response({
                       "Status":False,
                       "Message":"Required name"
                    })
                qs = qs.filter(ParentCode__exact=name).order_by('ItemName')

            elif option == 3:
                cnt_active = qs.filter(Enabled=1).count()
                cnt_inactive = qs.filter(Enabled=0).count()
                return Response(
                    {
                        "Active":cnt_active,
                        "In-active":cnt_inactive,
                    }
                )
            elif option ==4:
                l1_categorys = list(set(qs.values_list("CategoryL1",flat=True)))
                # l1_average = qs.filter(CategoryL1)
                l1_avg = []
                for l in l1_categorys:
                    avg = qs.filter(CategoryL1=l).aggregate(Avg('MRPrice'))
                    l1_avg.append({"category":l,"avg":avg})
                print("avg ", l1_avg)

                l2_categorys = list(set(qs.values_list("CategoryL2", flat=True)))

                l2_avg = []
                for l in l2_categorys:
                    avg = qs.filter(CategoryL2=l).aggregate(Avg('MRPrice'))
                    l2_avg.append({"category":l,"avg":avg})
                print("avg ", l2_avg[0])
                # l2_average =
                return Response(
                    {
                        "CategoryL1":[
                            l1_avg
                        ],
                        "CategoryL2":l2_avg
                    }
                )
            return Response(ItemSerializer(qs,many=True).data)

        else:
            return Response({
                "Status": False,
                "Message": "Invalid option",
                "Options": {
                    "option 0": "Load the products shown in the below excel using any excel reader library( or your own custom reader) of your choice",
                    "option 1": "Given a product name or product code, find the top-most parent of it by its name",
                    "option 2": "Given a product name, display the name of all of its children in sorted order.",
                    "option 3": "Display a count of active and in-active products.",
                    "option 4": "Display the value of average product price per Category L1 and Category L2",
                }
            })

    def patch(self, request, *args, **kwargs):
        "file name"
        file_name = '\items.xlsx'
        data = getExcellData(file_name)

        """
        0) Load the products shown in the below excel using any excel reader library (or your own custom reader) of your choice {completed}
        """

        return Response({
            "Status":True,
            "Message":"Success",
            "result":data
        })
    def delete(self,request):
        qs = ItemTable.objects.all().delete()

        return Response({
            "deleted"
        })
    def post(self,request):
        file_name = '\items.xlsx'

        data = getExcellData(file_name)

        # print(data[0])
        qs = ItemTable.objects.all()

        instances = []
        obj = {}
        with transaction.atomic():

            for index,item in enumerate(data,start=1):
                try:
                    obj = ItemTable(
                        ItemName=item['Item Name'],
                        ItemCode=item['Item Code'],
                        CategoryL1 = item['Category L1'],
                        CategoryL2 = item['Category L2'],
                        UPC = item['UPC'],
                        ParentCode = item['Parent Code'],
                        MRPrice = item['MRP Price'],
                        Size = item['Size'],
                        Enabled = 1 if item['Enabled'].lower() in ["yes","y"] else 0
                    )
                    obj.save()
                    status = True
                    message = "saved"
                except Exception as e:
                    print("Excepction occured : ",e)
                    status = False
                    message = f"Excepction occured : {e}"
                    break

        return Response({
            "Status":status,
            "Message":message
        })

def getExcellData(filename):
    "combining file with base dir path"
    file = str(BASE_DIR) + filename
    wb = load_workbook(filename=file)

    sheet_ranges = wb["source"]

    list_heading = []
    list_data = []

    for index, row in enumerate(sheet_ranges, start=1):
        data_dict = {}
        for jndex, item in enumerate(row, start=0):
            if index == 1:
                "To get label"
                list_heading.append(item.value)
            if index > 1:
                "formating data in to a dictionary"
                data_dict[list_heading[jndex]] = item.value
        "Adding formatted dictionary data in to array"
        if data_dict:
            list_data.append(data_dict)
    return list_data