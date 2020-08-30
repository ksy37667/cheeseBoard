import React, {useState} from 'react';
import axios from 'axios';
import useAsync from './useAsync';
import PaginationFunc from './Pagination';
import TableRow from '@material-ui/core/TableRow';
import TableHead from '@material-ui/core/TableHead';
import TableCell from '@material-ui/core/TableCell';
import Table from '@material-ui/core/Table';
import Moment from 'moment'
import Paper from '@material-ui/core/Paper'
import { makeStyles } from '@material-ui/core/styles';
import ButtonAppBar from './AppBar';
import Button from '@material-ui/core/Button';
import { Container } from '@material-ui/core';




const useStyles = makeStyles((theme) => ({
    root: {
        marginLeft: '100',
        marginRight: '100',
    },
    table: {
        marginTop: 50
    },
    refetchBtn: {
        marginTop: 5,
        marginBottom: 5,
        marginLeft: "auto"
        
    }
}));

const getBoards = async () => {
    const response = await axios.get('http://127.0.0.1:8000/boards/brd/');
    console.log(response.data);
    return response.data;
}

const Board = () => {
    const classes = useStyles();

    const [state, refetch] = useAsync(getBoards, []);
    const cellList = ['번호', '제목', '글쓴이','작성 시간'];
    const [currentPage, setCurrentPage] = useState(1);
    const [postsPerPage] = useState(10);

    const { loading, data: boards, error} = state;

    if (loading) return <div>로딩중</div>
    if (error) return <div>에러가 발생했습니다.</div>
    if (!boards) return null;

    const indexOfLastPost = currentPage * postsPerPage;
    const indexOfFirstPost = indexOfLastPost - postsPerPage;
    const currentPosts = boards['results'].slice(indexOfFirstPost, indexOfLastPost);

    const paginate = (pageNumber) => setCurrentPage(pageNumber);

    return (
        <div className={classes.root}>
            <ButtonAppBar/>
            <div style={{ display: "flex" }}>
                <Button className={classes.refetchBtn} onClick={refetch} variant="contained" color="primary">새로고침</Button>
            </div>
            <Paper>
                <Table className={classes.table}>
                    <TableHead className={classes.tableHead}>
                        <TableRow>
                            {cellList.map( c => {
                            return <TableCell>{c}</TableCell>
                            })}
                        </TableRow>
                    </TableHead>
                    {currentPosts.map(board => (
                        <TableRow key = {board.id}>
                        <TableCell>{board.id}</TableCell>
                        <TableCell>{board.title}</TableCell>
                        {/* <TableCell>{board.content}</TableCell> */}
                        <TableCell>{board.username}</TableCell>
                        <TableCell>{Moment(board.created_at).format('YYYY[-]MM[-]DD/ h:mm:ss a')}</TableCell>
                        </TableRow>
                    ))}
                    <PaginationFunc postsPerPage={postsPerPage} totalPosts={boards.count} paginate={paginate} />
                </Table>
            </Paper>
        </div>
        
    )
}

export default Board;