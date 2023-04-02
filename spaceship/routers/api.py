from fastapi import APIRouter
import numpy

router = APIRouter()


@router.get('/matrix')
def matrix() -> dict:
    matrix_A = numpy.random.rand(10, 10)
    matrix_B = numpy.random.rand(10, 10)
    product = numpy.matmul(matrix_A, matrix_B)

    result = {
        "matrix_A": matrix_A.tolist(),
        "matrix_B": matrix_B.tolist(),
        "product of matrices": product.tolist()
    }

    return result