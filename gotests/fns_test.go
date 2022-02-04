package gotests

import (
	"math/rand"
	"testing"
	"time"

	"github.com/stretchr/testify/require"
)

func TestAdd(t *testing.T) {
	tests := [][]int{
		{1, 1, 2},
		{1, -1, 0},
		{-1, -5, -6},
	}

	for _, tc := range tests {
		t.Run("sum", func(t *testing.T) {
			require.Equal(t, AddInt(tc[0], tc[1]), tc[2])
		})
	}
}

func TestFlaky(t *testing.T) {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	if n := r.Intn(100); n > 75 {
		t.Fatalf("Bad luck value was: %d", n)
	}
}

func TestAlwaysFail(t *testing.T) {
	t.Fail()
}
